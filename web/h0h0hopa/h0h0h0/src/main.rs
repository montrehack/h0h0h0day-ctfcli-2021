use warp::{Filter, Reply, reply::Response, http::HeaderMap};
use std::collections::HashMap;
use std::convert::Infallible;
use serde::{Serialize, Deserialize};
use std::fs::File;
use std::io::prelude::*;

#[derive(Serialize)]
struct OpaInput {
    headers: HashMap<String,String>,
    query_params: HashMap<String,String>
}

#[derive(Deserialize)]
struct IsSantaResult {
    result: bool
}

async fn check_santa(headers: HeaderMap, query_params: HashMap<String, String>) ->
    Result<IsSantaResult, reqwest::Error>
{
    let mut headers_hashmap = HashMap::new();
    for (key, value) in headers.iter() {
        headers_hashmap.insert(
            key.as_str().to_owned(),
            String::from_utf8_lossy(value.as_bytes()).into_owned());
    }

    let input = OpaInput {
        query_params: query_params,
        headers: headers_hashmap
    };
    let mut map = HashMap::new();
    map.insert("input", input);

    let client = reqwest::Client::new();
    let body = client
        .post("http://opa:8181/v1/data/policies/is_santa")
        .json(&map)
        .send()
        .await?
        .json::<IsSantaResult>()
        .await?;

    Ok(body)
}

fn read_file(filename: &str) -> std::io::Result<String> {
    let mut file = File::open(filename)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn show_result(filename : &str) -> Result<Response, Infallible> {
    match read_file(filename) {
        Ok(html) => Ok(warp::reply::html(html).into_response()),
        Err(error) => Ok(warp::reply::with_status(format!("An error occured: {}", error),
                                                  warp::http::StatusCode::INTERNAL_SERVER_ERROR).into_response())
    }
}

async fn handler(headers: HeaderMap, query_params: HashMap<String, String>) -> Result<impl Reply, Infallible> {
    match check_santa(headers, query_params).await {
        Ok(IsSantaResult {result: false}) => show_result("public/not_santa.html"),
        Ok(IsSantaResult {result: true}) => show_result("public/santa.html"),
        Err(error) => Ok(warp::reply::with_status(format!("An error occured: {}", error),
                                                  warp::http::StatusCode::INTERNAL_SERVER_ERROR).into_response())
    }
}

#[tokio::main]
async fn main() {
    let santa =
        warp::get()
        .and(warp::path::end())
        .and(warp::header::headers_cloned())
        .and(warp::query::<HashMap<String,String>>())
        .and_then(handler);

    let policies =
        warp::get()
        .and(warp::path("policies"))
        .and(warp::fs::file("public/policies.txt"));

    warp::serve(santa.or(policies))
        .run(([0, 0, 0, 0], 3030))
        .await;
}

