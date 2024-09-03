/* eslint-disable no-unused-vars */
import './App.css';
import Title from './title';
import AddBook from './addBook';
import React, { useState, useEffect } from 'react'


function App() {
// eslint-disable-next-line no-unused-vars
  const [data, setData] = useState([{}])


// eslint-disable-next-line no-unused-vars
  return (
    <div className="App">
      <Title></Title>
      <AddBook></AddBook>
    </div>
  );
}

export default App;
