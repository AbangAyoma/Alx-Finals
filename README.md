# WriteHub  

## Description  
**WriteHub** is a dynamic blog platform built with **Node.js** for the backend. It enables users to create, edit, and manage blog posts efficiently. The platform is designed to be responsive, making it accessible on both desktop and mobile devices.  

## Features  
- User authentication with secure session management.  
- CRUD operations for blog posts (Create, Read, Update, Delete).  
- Blog listing with pagination.  
- Search functionality for blog posts.  
- Mobile-friendly, responsive UI.  

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
| `/api/blogs`          | GET    | Fetch all blogs              |  
| `/api/blogs/:id`      | GET    | Fetch a single blog post     |  
| `/api/blogs`          | POST   | Create a new blog post       |  
| `/api/blogs/:id`      | PUT    | Update a blog post           |  
| `/api/blogs/:id`      | DELETE | Delete a blog post           |  

## Future Improvements  
- Add user profiles and avatars.  
- Implement comments and likes for blogs.  
- Add tags or categories for better content organization.  

## Acknowledgments  
Special thanks to the **ALX Program** for this amazing opportunity to grow and build practical skills.  
