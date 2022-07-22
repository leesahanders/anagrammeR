library(httr)
library(jsonlite)

GetWeather <- function(
    station_id = NULL,
    api_key = '6532d6454b8aa370768e63d6ba5a832e' # public key (don't fret)
) {
  
  baseURL <- "https://api.weather.com/v2/pws/observations/current?"
  requestURL <- paste0(baseURL,
                       "stationId=",
                       station_id,
                       "&format=json",
                       "&units=e",
                       "&apiKey=",
                       api_key)
  
  # Make the actual request to the API
  response <- httr::GET(requestURL)
  # Get the Status of the request
  status <- httr::http_status(response)
  # Get data
  if (status$message == "Success: (200) OK") {
    # Convert to JSON
    response_json <- httr::content(response, "text", encoding = "UTF-8")
    
    # Convert JSON into list object that we can separate and parse
    response_data <- jsonlite::fromJSON(response_json,
                                        simplifyVector = TRUE,
                                        flatten = TRUE)
    observations <- response_data$observations
  }
  
  return(observations)
  
}

# Here's how you pull it
stations <- c('KTXDALLA724', 'KWASEATT2743')

# Get a weather reading for each station and add it to the obs_df
for (id in stations) {
  GetWeather(id)
}
