# The Loggers

> Author: alexandre-lavoie

During the winter, Gérard and Robert Tremblay run a small log distribution business online. They use a custom solution from a few years back.

This year, there seems to be alot of weird internal traffic coming from the system. Can you figure out the issue? 

## Tags

- web

## Files

- ./dist/the-loggers-1.0.0.jar

## Depedencies

- `Java 8`

## Build WAR

Build the webserver with:

```
./gradlew build
```

The output can be found in `./build/libs`.

## Run WAR

```
java -jar /path/to/the-logger-*.war
```

## Build Docker

With a built WAR, you can build Docker image with typical commands:

```
docker build -t the-loggers .
```

## Run Docker

You can run the Docker image and expose the port:

```
docker run -p 8080:8080 -t the-loggers
```
