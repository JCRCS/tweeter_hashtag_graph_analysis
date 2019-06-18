# Twitter_hashtag_graph_analysis
this is a tool that fetch tweets from different context, in order to find the "hashtags" entities mofre significant between contexts

This is the user manual to deploy the application that is for Windows users

## Installation

Download and install [MongoDB Community Edition](https://docs.mongodb.com/v3.4/installation/) as the data base of the application, also you can download [Ghepi](https://gephi.org/users/download/) as a tool to analyze and visualize the graphs (.graphtml) that makes the application.

The application is stored [here](https://github.com/JCRCS/tweeter_hashtag_graph_analysis) you can clone the project with git.

```bash
git clone https://github.com/JCRCS/tweeter_hashtag_graph_analysis
```

the application comes with an environment (.env) of python, with all the packages that you are going to need in order to deploy the application

when you already download the application you have to go to the terminal and execute the python environment as:

```bash
>~.\.env\Scripts\activate.bat
```

once you are in the environment of python (your terminal path should start with "(.env)" ), you have to execute the main.py as:

```bash
~ >python main.py
```

there will be an menu and you have to follow the steps and you are ready to go.

## Tool classes design

![alt text](https://github.com/JCRCS/tweeter_hashtag_graph_analysis/blob/master/Storage/classes-model.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


