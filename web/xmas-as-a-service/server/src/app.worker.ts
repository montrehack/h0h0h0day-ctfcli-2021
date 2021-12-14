import { HttpException, HttpStatus } from "@nestjs/common";
import { exec, execSync } from "child_process";
import { Readable } from "stream";
import { v4 } from "uuid";

export class AppWorker {
  private _name: string;
  private _port_mapping: string;
  private _uuid: string;
  private _createdAt: Date;

  constructor(name: string, port_mapping: string) {
    this._name = name;
    this._port_mapping = port_mapping;
    this._uuid = v4();
  }

  public get uuid(): string {
    return this._uuid;
  }

  public get initialized(): boolean {
    return !!this._createdAt;
  }

  public get createdAt(): Date {
    return this._createdAt;
  }

  private _exec(cmd: string): Readable {
    if (/[\;\&\|\`]/g.test(cmd))
      throw new HttpException(
        "Invalid characters detected",
        HttpStatus.BAD_REQUEST,
      );
    return exec(cmd + " 2>&1").stdout;
  }

  public pull(): Readable {
    return this._exec(`docker pull ${this._name}`);
  }

  public logs(): Readable {
    return this._exec(`docker logs -f -n100 ${this._uuid}`);
  }

  public run(): Readable {
    this._createdAt = new Date();
    return this._exec(
      `docker run -p${this._port_mapping} -d -u1000 --restart=no --name ${this._uuid} ${this._name}`,
    );
  }

  public start(): Readable {
    return this._exec(`docker start ${this._uuid}`);
  }

  public stop(): Readable {
    return this._exec(`docker stop ${this._uuid}`);
  }

  public kill(): Readable {
    return this._exec(`docker kill ${this._uuid}`);
  }

  public health(): "dead" | "starting" | "healthy" | "unhealthy" {
    const match = /\((health.*?)\)/.exec(
      execSync(`docker ps --no-trunc --filter "name=${this._uuid}"`).toString(),
    );
    if (!match || !match[1]) return "dead";
    return match[1].split(" ").pop() as any;
  }

  public rm(): Readable {
    return this._exec(`docker rm -f -v ${this._uuid}`);
  }
}
