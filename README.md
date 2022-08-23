# Handie
Handie is an app for general contractors to manage clients, projects, and estimates. Created in Python using PySide6.
<br/>

**Tools: Python, PySide6, SQLite, ReportLab**

### Overview
The app is divided into four sections: Home, Customer, Project, and Estimates.
- Home page: The user can add new construction projects and view active projects and materials needed.
- Customer page: Via a table, the user can access and edit customer information.
- Projects page: The user can access, add, and edit project information.
- Estimates page: The user can access project estimates.
<br/>

![overview](https://user-images.githubusercontent.com/86685331/186224074-96fd4ba9-73c2-46d4-87e0-9d4a162aa5fe.gif)
<br/>

#### Home / Add project
User can look at active projects and add new projects.
<br/>
<br/>
Adding a new project:
- The user can choose between new or existing customer.
- If new customer:
  - The user can add customer information (name, address, city, phone, email).
- Add project info (project name, start date, end date).
- Choose construction area and tasks for that particular area.
- Add materials information (name, description, quantity, price).
<br/>

![add_project2](https://user-images.githubusercontent.com/86685331/186216993-807fe26a-9955-477c-b6e1-79e7ad456f0b.gif)

<br/>
After a project has been created it can be accessed and modified in the Projects section of the app.
<br/><br/>

![project_page](https://user-images.githubusercontent.com/86685331/186225734-b0f4eb4f-b3ec-4ce7-96fe-3aeded3d0bc2.gif)



#### Estimate
Once the user adds a new project, an estimate page is created. This page is divided between contractor and customer sections.
<br/>
<br/>
The contractor section has information that would only be viewed by the contractor. The customer section contains information that will be used 
to generate a PDF document for the customer.
On the estimate page:
- Materials cost, labor cost, fees, taxes, total cost (for contractor)
- Materials cost, labor cost, fees, total cost (for customer - values can differ from the contractor page and will appear in the PDF)
- Text fields for writing construction tasks and information according to selected tasks (will appear on the PDF)

![estimate](https://user-images.githubusercontent.com/86685331/186221633-2a385063-ad12-4489-9a14-a3bab747e89a.gif)


After an estimate is created, it can also be accessed and modified by going to the Estimates section of the app.

![estimate_page](https://user-images.githubusercontent.com/86685331/186227019-b2e0b8e3-e339-416d-8908-e8a1f1c1fb93.gif)





