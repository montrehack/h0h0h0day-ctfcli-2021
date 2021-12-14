FROM rust:1.57 as builder

WORKDIR /usr/src/h0h0h0
COPY . .

RUN cargo install --path .


FROM debian:buster-slim

WORKDIR /h0h0h0

EXPOSE 3030
RUN apt-get update && apt-get install -y libssl-dev && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/cargo/bin/h0h0h0 /h0h0h0/h0h0h0
COPY ./public /h0h0h0/public

CMD ["./h0h0h0"]
