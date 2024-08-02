# IBM call_for_code_2022

This repo is created as part of a competition IBM Call for Code 2022 and is contributed by the EY internal team members.


## Usage 
Running `create_co2_footprint_estimator.sh` will train and run a simple app that would provide the information regarding 
the carbon footprint that the user would be leaving behind when carrying out a task. The input will be raw text and it will be
the task the user is going to perform. The NER model would then identify the entities inside the task input by the user
to provide them with the information of carbon footprint that particular activity would be creating.

## Technical Details

In the backend is a flask app that consumes a list of tasks in the form of txt file and detects the hardcoded entities i.e food,
clothing etc from it and maps it to hardcoded carbon footprint values associated with each entity detected. The carbon
footprint values for the time being are dummy values and are hardcoded as well.
