require 'sinatra'
require 'sqlite3'

DB = SQLite3::Database.new("db.sqlite3") 
HTML = DATA.read

get '/' do 
  HTML
end

get '/check' do
  name = params[:name]

  nice_chars = ('a'..'z').to_a
  naughty_chars = (0x00..0xff).map(&:chr) - nice_chars

  naughty = naughty_chars.any? do |naughty_char|
    name.include?(naughty_char)
  end

  if naughty
    'very naughty'
  else
    DB.execute("select nice('#{name}')")[0]
  end
end

get '/source.rb' do
  content_type 'text/plain'
  File.read(__FILE__)
end

DB.create_function("nice", 1) do |func, value|
  func.result = if value.hash.even?
    "nice"
  else
    "naughty"
  end
end

__END__
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>santacheck</title>
  </head>
  <body bgcolor="ac2121" text="ffffff" background="https://i.ibb.co/0ZCtRmr/snow02.gif">
    <div style="margin-top: 5%;">
      <center>
        <img src="https://i.ibb.co/h2FYWYy/animated-santa-claus-image-0283.gif" />
        <p>Naughty or nice? Check your name with santa</p>
        <input type="text" placeholder="Name" />
        <button>Check</button>
        <p>
          <a href="/source.rb" style="color: rgba(255,255,255,0.7)">Source</a>
        </p>
      </center>
    </div>
    <script>document.querySelector("input").onchange=(e)=>fetch(`/check?name=${e.target.value}`).then(x=>x.text()).then(x=>document.querySelector('p').innerText=x)</script>
  </body>
</html>
