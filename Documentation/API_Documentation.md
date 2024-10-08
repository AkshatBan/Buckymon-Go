# API Documentation 

## Description  
This document describes the endpoints through which the frontend and backend will communicate 
and the format which the data is expected to be passed, as well as any errors that can occur.

## Base Url  
The base Url for that the backend will post to and the frontend will fetch from is 

`http://127.0.0.1:5000/api`

(Note: this is subject to change)

## Currently Supported Requests (as of 4/23/24)  

### GET /Get_List_Of_Locations

Returns a list of location data with each location with the following format

```
{
    id: 1,
    lat: 43.0719,
    long: -89.408,
    location_name: 'Union South',
    event_desc: 'description of even happening at this location'
    event_id: 40000001
}
```
```
Upon successful request, the backend returns code **200** and the following message
```
{
    message: "Data received successfully"
}
```

## Requests to Be Implemented  

```
### POST /Login_User

In order to login the user will be prompted for their username. There will be no authentification of the user.
The frontend will pass this to the backend to attempt login with the following body

```
{
    username: 'user123'
}
```

Upon success the backend will log the user in, return code **200**, and the following body

```
{
    username: 'user123',
    message: 'successfully logged in'
}
```

If no username is provided the backend will return code **400** with body

```
{
    message: 'No username provided'
}
```


### GET /User_Achievements

Get achievements that user has completed and their game score, only requested when a user is logged in
The following request body will be sent

```
{
    username: 'user123'
}
```

The backend will return the following json body with achievement data assosciated with the logged in user, and code **200**

```
{
    username: 'user123',
    user_score: 1,
    completed_achievements:[
        {
            achievement_id: 1,
            achievement_name: 'example achievement1',
            achievement_score: 3,
            achievement_description: 'example description1'
        },
        {
            achievement_id: 2,
            achievement_name: 'example achievement2',
            achievement_score: 4,
            achievement_description: 'example description2'
        }
    ]
}
```

Note: the list of completed achievements can be any length

### POST /Complete_Event

When the user completes an event a post will be sent to the backend with the following body  

```
{
    username: 'user123',
    event_id: 1
}
```

In response, the backend will send code **200** along with the following body  

```
{
    updated_score: old_score + event_score
}
```

If the user and that event have already been completed, the backend will send error code **400** 

### GET /Active_Events  

This will return a list of active events that the user can seek out the complete, request body as follows 

```
{
    username: 'user123'
}
```

The backend will return a list of events that the user has **NOT** completed yet, each event will have the following format  

```
{
    event_id: 1,
    lat: 43.0719,
    long: -89.408,
    location_name: 'Union South',
    event_score: 3,
    event_name: "Name of Event"
    event_description: 'sample event description'
}
```

If the user has no more events to complete, then the backend will send error code **400**

### GET /Get_Completed_Events 

This will return a list of events that the user has already completed, request body as follows 

```
{
    username: 'user123'
}
```

The backend will return a list of events that the user has **ALREADY** completed yet, each event will have the following format  

```
{
    event_id: 1,
    lat: 43.0719,
    long: -89.408,
    location_name: 'Union South',
    event_score: 3,
    event_name: "Name of Event"
    event_description: 'sample event description'
}
```

If the user has not completed any events, then the backend will send error code **400**

