import {
  Body,
  Controller,
  Get,
  Param,
  Post,
  Res,
  Response,
} from "@nestjs/common";
import { AppService } from "./app.service";

@Controller("/api")
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post("/spawn")
  spawn(
    @Body("name") name: string,
    @Body("port") port: number,
  ): { uuid: string; port: number; exp: number } {
    return this.appService.spawn(name, port);
  }

  @Get("/remove/:uuid")
  remove(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.remove(uuid).pipe(res as any);
  }

  @Get("/logs/:uuid")
  logs(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.logs(uuid).pipe(res as any);
  }

  @Get("/run/:uuid")
  run(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.run(uuid).pipe(res as any);
  }

  @Get("/start/:uuid")
  start(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.start(uuid).pipe(res as any);
  }

  @Get("/stop/:uuid")
  stop(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.stop(uuid).pipe(res as any);
  }

  @Get("/kill/:uuid")
  kill(@Param("uuid") uuid: string, @Res() res: Response): void {
    this.appService.kill(uuid).pipe(res as any);
  }

  @Get("/health/:uuid")
  health(
    @Param("uuid") uuid: string,
  ): "dead" | "starting" | "healthy" | "unhealthy" {
    return this.appService.health(uuid);
  }
}
