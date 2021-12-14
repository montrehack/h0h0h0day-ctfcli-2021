FROM ruby:2.7-alpine

RUN apk add --no-cache build-base sqlite sqlite-dev sqlite-libs

COPY Gemfile Gemfile.lock app.rb db.sqlite3 /

RUN bundle

CMD ruby app.rb -p 4567 -o 0.0.0.0
