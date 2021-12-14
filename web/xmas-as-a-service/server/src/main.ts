import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    next();
  });

  await app.listen(3000);
}
bootstrap();
