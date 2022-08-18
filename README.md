# Handie
Handie is an app for general contractors to manage clients, projects, and estimates. Created in Python using PySide6.
<br/>

**Tools: Python, PySide6, SQLite, ReportLab**

### Overview
The app is divided into Home, Customer, Project, and Estimates.
- Home page: User can add new construction projects, and look at active projects and materials needed.
- Customer page: Through a table, user can access and edit customer information.
- Projects page: User can access, add, and edit project information.
- Estimates page: User can access project's estimates.
<br/>

![ezgif com-gif-maker](https://user-images.githubusercontent.com/86685331/184932754-240b2fc9-fc21-414c-8610-ad64e562a951.gif)
<br/>

#### Home/ Add project
User can look at active projects and add new projects.
<br/>
<br/>
Adding a new project:
- User can choose between new or existing customer.
- If new customer:
  - Can add customer info (name, address, city, phone, email).
- Add project info (project name, beggining date, end date).
- Choose construction area, and tasks for that particular area.
- Add materials info (name, description, quantity, price).
<br/>
<br/>
<br/>
<br/>
<br/>
After a project has already been created, it can be accessed and modified in the Projects session of the app.
<br/><br/><br/>




#### Estimate
After a user add a new project, an estimate page is created. The estimate page is divided into contractor and customer sections.
<br/>
<br/>
The contractor session has information which will be seen only by the contractor. The customer session contains information which will be used 
to generate a PDF form for the customer.
On the estimate page:
- Materials cost, labor cost, fees, taxes, total cost (for contractor)
- Materials cost, labor cost, fees, total cost (for customer - can have different values and will be used to print PDF)
- Text fields for writing construction tasks and info according to selected tasks (will be printed on PDF)
<br/>
<br/>
<br/>



After an estimate is created, it can also be accessed and modified by going to the Estimates part of the app.






