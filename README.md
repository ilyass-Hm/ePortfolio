# Ilyass Hmamou ePortfolio

## Table of content
  [Self-Introduction](https://github.com/ilyass-Hm/ePortfolio/blob/main/README.md#self-introduction)
  
  [Project Introduction: Artifacts Selection](https://github.com/ilyass-Hm/ePortfolio#project-introduction-artifacts-selection)
  
  [Code Review](https://github.com/ilyass-Hm/ePortfolio#code-review)
  
  [Enhancement One: Software Design and Engineering](https://github.com/ilyass-Hm/ePortfolio#enhancement-one-software-design-and-engineering)
  
  [Enhancement Two: Algorithm and data structure](https://github.com/ilyass-Hm/ePortfolio#enhancement-two-algorithm-and-data-structure)
  
  [Enhancement Three: Databases](https://github.com/ilyass-Hm/ePortfolio#enhancement-three-databases)
  
  [Self Reflection](https://github.com/ilyass-Hm/ePortfolio#self-reflection)
  
## Self-Introduction:
  I am Ilyass Hmamou, currently a computer science undergraduate in my final term, about to graduate. For the past six years, I've had a professional career in the software industry, starting as a software engineer and later transitioning into the role of a software solution architect.

  I have been in the computer science program for approximately eight years. I started with an associate's degree from a two-year college, leading to my first job as a software engineer. After a few years, I realized my ambition to attain a bachelor's degree and thus transferred my credits to SNHU. For the past four years, I've been steadily taking one or two classes each term to finally graduate at the end of this year, 2023.
While a significant portion of my knowledge and skills was acquired through hands-on professional experience, enrolling in the academic program has notably enhanced my problem-solving abilities. It has also introduced me to a variety of interesting tools outside my usual work domain and deepened my understanding of fundamental tasks, such as class design and database architecture, which I previously executed instinctively.
Looking forward, my career goals primarily revolve around securing positions in engineering management. Although my current role as a software solution architect is an important step in that direction, I believe that furthering my education in computer science with an advanced degree will be invaluable. 

## Project Introduction: Artifacts Selection

 For the final project, the requirement involves evaluating one to three artifacts that I have previously developed in either coursework or a professional setting. Subsequently, I am tasked with implementing three improvements to the chosen artifact(s). The first enhancement should pertain to Software Design and Engineering, the second one focuses on Algorithms and Data Structures, and the final improvement is associated with Databases.
 
  I decided to choose the "Salvare Search For Rescue App." as my artifact. It was developed during the period between September 2023 and October 2023 as a component of the final project for CS-340: Client/Server development course. 
The application enables users to engage with data from an existing animal shelter database through two distinct methods: an interactive data table equipped with built-in filters, and an interactive map within a user-friendly interface. Constructed with the utilization of the Python language, pyMongo driver, Dash framework, and MongoDB, the app provides a comprehensive user experience.

## Code Review

When I started reviewing the Artifacts I worked on in the past, I found out that this particular artifact -"Salvare Search For Rescue App."- lies in its capacity to demonstrate proficiency in all the three categories required by this course. The application was developed in adherence to object-oriented programming principles, which involve organizing objects into distinct classes and implementing CRUD operations specific to each object. Additionally, it serves as a testament to skills associated with full-stack development, encompassing back-end, front-end, and database implementation.

This artifact also offers promising prospects for improvement, enabling me to demonstrate my capability in analyzing existing projects, identifying weaknesses, and implementing effective solutions.

## Enhancement One: Software Design and Engineering 

The enhancement of this artifact required two significant actions. The initial step involved replicating the project locally, a critical measure that affords complete control over the development environment. This not only facilitates the current enhancement but also lays the groundwork for future improvements, particularly in the context of the upcoming database enhancement. This action item showcases proficiency in the DevOps domain, encompassing the establishment of a Python virtual environment, configuring MongoDB, importing requisite libraries, and integrating the database.

The second step pertains to updates in the code, encompassing both front-end and back-end modifications. Front-end updates focused on enhancing the interface for improved user-friendliness and introducing additional functionalities, such as buttons for filtering by animal type—a feature absent in the original build. On the back end, a server-side filtering mechanism was implemented to enable users to filter data by animal type directly from the backend, as opposed to relying on client-side filtering within the browser UI. The rationale behind this update is to enhance the application's performance, recognizing that app servers typically possess more computational power than client machines, where client-side filtering typically occurs.

## Enhancement Two: Algorithm and data structure

The focus of this enhancement was to improve the Algorithm used on the server-side filtering logic, which will lead to improving the efficiency of the code. This code improvement plan was around eliminating a nested if-elif block in the update_dashboard() method and replacing it with a switch case like logic; this change required the usage of dictionary data structure since Python doesn’t have a built-in switch case statement, therefore, I used a dictionary to map cases to functions, and provide a similar case of switch case.

## Enhancement Three: Databases

For the databases category, the improvement centered on transferring the data to a cloud server and establishing a straightforward method to link to the server and engage with the data through a third-party integrated UI tool. 

This enhancement provides advantages in terms of scalability, accessibility, cost efficiency, reliability, security, automated maintenance, integration capabilities, and faster deployment, making it a popular choice for many organizations and projects. It also contributes to a user-friendly experience for individuals who may not possess technical knowledge, offering them reliable, secure, and accessible access to applications and data.

## Self Reflection

Revising existing projects and code poses a constant challenge; developers often find creating and implementing new code more preferable than attempting updates on existing ones. The preference for new code arises from the opportunity to initiate a fresh design and develop new code for projects, free from legacy issues or connections.

During this process, I revisited my previous course documents to review the project and its relevant material. This review was crucial for gaining a deeper understanding and facilitating the implementation of changes and enhancements to the application.

The primary lesson derived from this experience underscores the importance of maintaining thorough documentation for a project and incorporating clear code comments. Effective documentation and meaningful comments prove invaluable when modifications are necessary. Code lacking meaningful comments becomes notably challenging to comprehend, let alone enhance.  

