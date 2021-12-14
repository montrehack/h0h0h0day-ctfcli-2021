import { HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { Readable } from "stream";
import { AppWorker } from "./app.worker";

const CONTAINER_DURATION = +process.env.CONTAINER_DURATION || 5 * 60 * 1000;
const MINIMUM_PORT = +process.env.MINIMUM_PORT || 3001;
const MAXIMUM_PORT = +process.env.MAXIMUM_PORT || 4001;
let CURRENT_PORT_INDEX = 0;

@Injectable()
export class AppService {
  private _workers: { [key: string]: AppWorker } = {};

  constructor() {
    // Remove old images
    setInterval(() => {
      const limit = new Date(Date.now() + CONTAINER_DURATION);
      for (const uuid in this._workers) {
        const worker = this._workers[uuid];
        if (!worker.initialized) continue;
        if (worker.createdAt > limit) {
          delete this._workers[uuid];
          worker.rm();
        }
      }
    }, 5 * 60 * 1000);
  }

  spawn(
    name: string,
    guest_port: number,
  ): { uuid: string; port: number; exp: number } {
    if (!name || !guest_port)
      throw new HttpException("Invalid parameters", HttpStatus.BAD_REQUEST);
    if (!/[A-z0-9\/\-\_\:\.]+/.test(name))
      throw new HttpException("Invalid image name", HttpStatus.BAD_REQUEST);

    const host_port =
      (CURRENT_PORT_INDEX++ % (MAXIMUM_PORT - MINIMUM_PORT)) + MINIMUM_PORT;
    const worker = new AppWorker(name, `${host_port}:${guest_port}`);
    this._workers[worker.uuid] = worker;

    // Remove left over sessions
    setTimeout(() => {
      if (!worker.initialized) delete this._workers[worker.uuid];
    }, 5 * 60 * 1000);
    return {
      uuid: worker.uuid,
      port: host_port,
      exp: Date.now() + CONTAINER_DURATION,
    };
  }

  remove(uuid: string) {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    const worker = this._workers[uuid];
    delete this._workers[uuid];
    return worker.rm();
  }

  run(uuid: string): Readable {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].run();
  }

  start(uuid: string): Readable {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].start();
  }

  stop(uuid: string): Readable {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].stop();
  }

  logs(uuid: string): Readable {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].logs();
  }

  kill(uuid: string): Readable {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].kill();
  }

  health(uuid: string): "dead" | "starting" | "healthy" | "unhealthy" {
    if (!this._workers[uuid])
      throw new HttpException("Worker not found", HttpStatus.NOT_FOUND);
    return this._workers[uuid].health();
  }
}
