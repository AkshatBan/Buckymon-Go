# Requirements and Specification Document

## TeamName

<!--The name of your team.-->

### Project Abstract

<!--A one paragraph summary of what the software will do.-->

geocaching app with added game element, with a focus on UW-Madison events/activities

Create an application to allow users to play “Buckymon Go!” This game would require users to go to various real world locations / events around the UW-Madison campus to earn points for capturing pictures (and possibly performing some mini-game task) at these locations / events. (Ideally, GPS would be used so that the users could capture/collect virtual things that exist only in proximity to the "target" coordinates. Another possibility: Use image analysis to automatically confirm that the picture they've taken corresponds to the objective.)

Users should earn points for achieving goals in the app and should have a saved library of all their accomplishments. The game should have a server that can service multiple users simultaneously.

Stretch: An interface where people holding events can enter a request to have a BG goal at their event; and a corresponding admin interface for processing those requests.

### Customer

<!--A brief description of the customer for this software, both in general (the population who might eventually use such a system) and specifically for this document (the customer(s) who informed this document). Every project will have a customer from the CS506 instructional staff. Requirements should not be derived simply from discussion among team members. Ideally your customer should not only talk to you about requirements but also be excited later in the semester to use the system.-->

### User Requirements

<!--This section lists the behavior that the users see. This information needs to be presented in a logical, organized fashion. It is most helpful if this section is organized in outline form: a bullet list of major topics (e.g., one for each kind of user, or each major piece of system functionality) each with some number of subtopics.-->

| ID   | Description                                                  | Priority | Status | Test Plan |
| ---- | ------------------------------------------------------------ | -------- | ------ | --------- |
| R11  | The frontend should display a login portal that prompts user to create an account to sign in for identification. | Low - Med      | Open   | Ensure login portal displays properly, including the Google sign in button and sign-up button. For account creation, check that the backend returns code 200 with the message "successfully logged in" upon success, otherwise, it will return code 409 due to duplicate username upon failure. |
| R12  | The frontend should display a map of a user's surrounding area with markers for nearby areas with activities. | High     | Open   | Check that the backend returns a list of uncompleted events of user in the format, according to the API Documentation. |
| R13  | The frontend should allow users to select a marker on map and display the activity with directions to the marker. It must also be verified from a few different locations from campus to verify directions. | High     | Open   | Create print statements to show that the correct location was selected with corresponding activities. |
| R14  | A section or tab in the web app that displays a user's past completed history, including a user's achievements and game score. | High     | Open   | Check if backend successfully gets the data of completed events. Next verify that the backend successfully sends the data to the frontend, and that the frontend receives properly. Then ensure that the user's completed events are displayed correctly, including format and correct data. |
| R15  | Have the backend handle multiple users intereacting with the app at the same time | Med     | Open   | Make a seperate array of active users and print them as output on console. |
| R16 | The frontend should send a request to the backend upon a user completing an event to log that event in user's completed history. | High     | Open   | Ensure that the backend receives the location data of the completed event. Upon success, check that it returns the following message, "Data received successfully". |
| R17 | The frontend should successfully log the user in to have access to their completed events and future data. | Med. - High | Open | Check upon successful login that the frontend returns the following message, "successfully logged in", along with code 200, otherwise, return code 400 with the following message, "username not registered" or code 401 with the message "password does not match username provided" upon failure. |
| R18 | Upon a user's request, the main page should display a map of user's current location for user to see nearby locations with uncompleted events. | High | Closed | Ensure that coordinates are set correctly. |

<div align="center"><small><i>Excerpt from Crookshanks Table 2-2 showing example user requirements for a timekeeping system</i></small></div>

- You 
  - Can
    - Use
- Bullet
  - Points
    - In
    - Markdown

### Use Cases & User Stories

<!--Use cases and user stories that support the user requirements in the previous section. The use cases should be based off user stories. Every major scenario should be represented by a use case, and every use case should say something not already illustrated by the other use cases. Diagrams (such as sequence charts) are encouraged. Ask the customer what are the most important use cases to implement by the deadline. You can have a total ordering, or mark use cases with “must have,” “useful,” or “optional.” For each use case you may list one or more concrete acceptance tests (concrete scenarios that the customer will try to see if the use case is implemented).-->

Here is a sample user story from [Clean Agile](https://learning-oreilly-com.ezproxy.library.wisc.edu/library/view/clean-agile-back/9780135782002/ch03.xhtml#ch03lev1sec1) using a markdown block quote:

> As the driver of a car, in order to increase my velocity, I will press my foot harder on the accelerator pedal.

1. You
   1. Can
      1. Also
2. Use
   1. Numbered
      1. Lists

### Decommission User Stories

Here is an example of an issue/user story to be decommissioned:

> DECOMMISSION: Implement User Authentication to Frontend.

Be sure to add a small comment to the issue to add more clarity of decommissioning it.

### User Interface Requirements

<!--Describes any customer user interface requirements including graphical user interface requirements as well as data exchange format requirements. This also should include necessary reporting and other forms of human readable input and output. This should focus on how the feature or product and user interact to create the desired workflow. Describing your intended interface as “easy” or “intuitive” will get you nowhere unless it is accompanied by details.-->

<!--NOTE: Please include illustrations or screenshots of what your user interface would look like -- even if they’re rough -- and interleave it with your description.-->

Images can be included with `![alt_text](image_path)`

### Security Requirements

<!--Discuss what security requirements are necessary and why. Are there privacy or confidentiality issues? Is your system vulnerable to denial-of-service attacks?-->

### System Requirements

<!--List here all of the external entities, other than users, on which your system will depend. For example, if your system inter-operates with sendmail, or if you will depend on Apache for the web server, or if you must target both Unix and Windows, list those requirements here. List also memory requirements, performance/speed requirements, data capacity requirements, if applicable.-->

| You    |    can    |    also |
| ------ | :-------: | ------: |
| change |    how    | columns |
| are    | justified |         |

### Specification

<!--A detailed specification of the system. UML, or other diagrams, such as finite automata, or other appropriate specification formalisms, are encouraged over natural language.-->

<!--Include sections, for example, illustrating the database architecture (with, for example, an ERD).-->

<!--Included below are some sample diagrams, including some example tech stack diagrams.-->

You can make headings at different levels by writing `# Heading` with the number of `#` corresponding to the heading level (e.g. `## h2`).

#### Technology Stack

Here are some sample technology stacks that you can use for inspiration:



```mermaid
flowchart RL
subgraph Front End
	A(Javascript: React)
end
	
subgraph Back End
	B(Python: Flask)
end
	
subgraph Database
	C[(MySQL)]
end

A <-->|"REST API"| B
B <-->|SQLAlchemy| C
```






#### Database

Database schema based on ER-Diagram (bold for primary key, italics for foreign key)

User(**user_id**, name, score)  
Achievements(**achievement_id**, a_name, a_description, a_score)  
Achieved(**user_id**, **achievement_id**)  
Events(**event_id**, _location_id_, e_name, e_score)  
Completed(**user_id**, **event_id**)  
Locations(**location_id** lat, long, l_name)


#### Class Diagram

```mermaid
---
title: Sample Class Diagram for Animal Program
---
classDiagram
    class Animal {
        - String name
        + Animal(String name)
        + void setName(String name)
        + String getName()
        + void makeSound()
    }
    class Dog {
        + Dog(String name)
        + void makeSound()
    }
    class Cat {
        + Cat(String name)
        + void makeSound()
    }
    class Bird {
        + Bird(String name)
        + void makeSound()
    }
    Animal <|-- Dog
    Animal <|-- Cat
    Animal <|-- Bird
```

#### Flowchart

```mermaid
---
title: Sample Program Flowchart
---
graph TD;
    Start([Start]) --> Input_Data[/Input Data/];
    Input_Data --> Process_Data[Process Data];
    Process_Data --> Validate_Data{Validate Data};
    Validate_Data -->|Valid| Process_Valid_Data[Process Valid Data];
    Validate_Data -->|Invalid| Error_Message[/Error Message/];
    Process_Valid_Data --> Analyze_Data[Analyze Data];
    Analyze_Data --> Generate_Output[Generate Output];
    Generate_Output --> Display_Output[/Display Output/];
    Display_Output --> End([End]);
    Error_Message --> End;
```

#### Behavior

```mermaid
---
title: Sample State Diagram For Coffee Application
---
stateDiagram
    [*] --> Ready
    Ready --> Brewing : Start Brewing
    Brewing --> Ready : Brew Complete
    Brewing --> WaterLowError : Water Low
    WaterLowError --> Ready : Refill Water
    Brewing --> BeansLowError : Beans Low
    BeansLowError --> Ready : Refill Beans
```

#### Sequence Diagram

```mermaid
sequenceDiagram

participant ReactFrontend
participant DjangoBackend
participant MySQLDatabase

ReactFrontend ->> DjangoBackend: HTTP Request (e.g., GET /api/data)
activate DjangoBackend

DjangoBackend ->> MySQLDatabase: Query (e.g., SELECT * FROM data_table)
activate MySQLDatabase

MySQLDatabase -->> DjangoBackend: Result Set
deactivate MySQLDatabase

DjangoBackend -->> ReactFrontend: JSON Response
deactivate DjangoBackend
```

## Standards & Conventions

### Variable Naming Convention 
- Variable Names: Are to be defined with snake case with lower case letters for example `let geolocation_from_user = 10;`
- Function Names: Are to follow the same snake case with _ seperator but the start of each word should be capitalized for example: `def Get_User_Info:`

### White Space / Line Length Convention
- Line Limit: Line length is not to exceed 80 charachters
- Whitespace Around Operators: Surround assignment(=) and boolean operators with one space on either side 
- Indentation: Use 4 spaces for Indentation
- Blank Lines: Use blank lines to separate logical blocks in methods
inspired by: "https://google.github.io/styleguide/pyguide.html"

### Comment Blocks
Write a big comment block at the start of each function in the following format:
```
/*
* What this function does
* What this function does
* Params and info about them
* Return value and how it is intended to be used
*/
```
The * character acts like a bullet point and this way we will be easily able to understand other people's functions in a black. box way.

If your function is long in length then adding smaller comment blocks at the start of each segment is highly recommended; for example:
```
function abc(x, y, z){
    //The code below gets image from the camera
    --------------
    --------------
    --------------
    --------------
    --------------

    //The segment handles moving the data to the DjangoBackend
    --------------
    --------------
    --------------
    --------------
    --------------

    //The final segment is responsible for moving the backend processed data to the ReactFrontend
    --------------
    --------------
    --------------
    --------------
    return value;
}
```

### Branch Naming Convention
When creating a new branch use the following convention, initial + forward slash + name of feauture. For example, `AA/issue4` for user Agastya Asthana working on Issue #4.

### Closing Issues in GitLab
As we move issues to the workflow columns on the sprint board (workflow::in_progress and workflow::blocked), those workflow labels get added to the issue's list of labels. When closing the issues, make sure to deselect these workflow labels in an effort to avoid confusion.

Also make sure to re-evaluate your weight estimations and modify them with the amount of time the issue actually took. This will help us get better at our estimations and also ensure that we accurately track everyone's project contributions.


<!--Here you can document your coding standards and conventions. This includes decisions about naming, style guides, etc.-->
