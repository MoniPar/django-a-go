




# TAILOR'S THIMBLE

Tailor's Thimble is a responsive website built for a fictitional tailoring business.  

It provides the user value in learning about the business and the services it provides.  It also has a booking facility by which users can schedule, view, edit and delete appointments.  

![Am I responsive image]()

![Link to the live website]()

## Table of Contents
* [Overview](#overview)
* [User Experience (UX)](#user-experience-ux)
    * [Strategy / Site Goals](#strategy--site-goals)
    * [Scope / User Stories](#scope--user-stories)
    * [Structure / Design Choices](#structure--design-choices)
    * [Skeleton / Wireframes](#skeleton--wireframes)
    * [Surface](#surface)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
    * [Development Bugs](#development-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

[Back To Top](#tailors-thimble)

____

## Overview

[Back To Top](#table-of-contents)

____

## User Experience (UX)

### Strategy / Site Goals
### Scope / User Stories
### Structure / Design Choices
### Skeleton / Wireframes
### Surface

[Back To Top](#table-of-contents)

____

## Features

### Existing Features
### Future Features

[Back To Top](#table-of-contents)

_____

## Technologies Used

[Back To Top](#table-of-contents)

____

## Testing

### Development Bugs


* **Admin Panel**

Issue: Trying to add 'user' as a field in `search_fields` in the "AppointmentAdmin" class. 

Error: FieldError - Related Field got invalid lookup: icontains

Solution: Found on [this blog article by Jess Brown.](https://notdefined.tech/blog/how-to-fix-django-error-related-field-got-invalid-lookup-icontains/) Since the 'user' field is a ForeignKey, a text search cannot be done on it so it needed to be changed to include a text-based field that belongs to 'user'.  To do this a double underscore was needed to tell Django to grab the 'username' field from the 'user'. 
`search_fields = ("user_username", ...)`

[Back To Top](#table-of-contents)

____

## Deployment

[Back To Top](#table-of-contents)

____

## Credits

[Back To Top](#table-of-contents)

____

## Acknowledgements


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


[Back To Top](#table-of-contents)

____


