import jsonServer from 'json-server';
import cors from 'cors'; 
import express from 'express'; 
import fs from 'fs';
const server = express();
const dbFile = 'db.json';
const rawData = fs.readFileSync(dbFile);
const db = JSON.parse(rawData);

server.use(
   cors({
     origin: '*',
     credentials: true, 
   })
 );

// Custom routes for authentication
server.post('/login', (req, res) => {
   const { username, password } = req.body;
   const user = db.users.find((u) => u.username === username && u.password === password);
   if (user) {
     res.header('Access-Control-Allow-Origin', '*');
     res.header('Access-Control-Allow-Credentials', 'true');
     res.status(200).json({ message: 'ok', user });
   } else {
     res.status(401).json({ message: 'not ok' });
   }
 });
 
 server.post('/logout', (req, res) => {
   res.status(200).json({ message: 'Logout successful' });
 });
 
 server.put('/update-profile', (req, res) => {
   res.status(200).json({ message: 'Profile updated successfully' });
 });
 
 const port = 3001;
 server.listen(port, () => {
   console.log(`JSON Server is running on port ${port}`);
 });