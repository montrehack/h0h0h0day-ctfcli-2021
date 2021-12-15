FROM gradle:7.3.1-jdk17-alpine AS builder
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --no-daemon

FROM openjdk:8u181-jdk-alpine
RUN apk add curl wget
WORKDIR /challenge
COPY --from=builder /home/gradle/src/build/libs/*.war app.war
RUN chmod 444 app.war
COPY docker/flag.txt flag.txt
RUN chmod 444 flag.txt
ENV port=8080
RUN addgroup -S challenge 
RUN adduser -S challenge -G challenge
USER challenge
ENTRYPOINT ["java","-jar","/challenge/app.war"]
