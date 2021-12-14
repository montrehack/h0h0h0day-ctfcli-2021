import { Module } from "@nestjs/common";
import { ServeStaticModule } from "@nestjs/serve-static";
import { join as path_join } from "path";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";

@Module({
  imports: [
    ServeStaticModule.forRoot({
      rootPath: path_join(__dirname, "./public"),
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
