# TechSphere  

## Description  
**TechSphere** is a dynamic tech blog platform built with **Node.js** for the backend. It provides a space for users to write, share, and discuss tech-related topics, similar to Medium. Users can post articles, read others' posts, and interact with the content. The platform is designed to be responsive, making it accessible across various devices.  

## Features  
- User authentication for secure access and session management.  
- CRUD operations for blog posts (Create, Read, Update, Delete).  
- Tech blog listing with pagination and search functionality.  
- Responsive design for mobile and desktop viewing.  
- User-friendly interface with options to like and comment on posts.  

## Tech Stack  
- **Front-end:** HTML, CSS, JavaScript  
- **Back-end:** Node.js (Express.js)  
- **Database:** MySQL  

## Installation and Usage  
1. Clone this repository:  
   ```bash  
   git clone git@github.com:AbangAyoma/Alx-Finals.git  
   cd Alx-Finals  
   ```  

2. Install dependencies:  
   ```bash  
   npm install  
   ```  

3. Set up environment variables in a `.env` file:  
   ```plaintext  
   DB_HOST=your-database-host  
   DB_USER=your-database-username  
   DB_PASSWORD=your-database-password  
   DB_NAME=your-database-name  
   PORT=3000  
   JWT_SECRET=your-secret-key  
   ```  

4. Start the application:  
   ```bash  
   npm start  
   ```  

5. Open your browser and navigate to: `http://localhost:3000`.  

## Endpoints Overview  
| Endpoint              | Method | Description                  |  
|-----------------------|--------|------------------------------|  
| `/api/auth/register`  | POST   | Register a new user          |  
| `/api/auth/login`     | POST   | User login                   |  
| `/api/posts`          | GET    | Fetch all tech posts         |  
| `/api/posts/:id`      | GET    | Fetch a single tech post     |  
| `/api/posts`          | POST   | Create a new tech post       |  
| `/api/posts/:id`      | PUT    | Update a tech post           |  
| `/api/posts/:id`      | DELETE | Delete a tech post           |  

## Future Improvements  
- Implement post categories and tags for better content organization.  
- Add user profiles with personal settings and avatars.  
- Implement comment sections and like/dislike functionality for posts.  

## Acknowledgments  
Special thanks to the **ALX Program** for this amazing opportunity to grow and build practical skills.