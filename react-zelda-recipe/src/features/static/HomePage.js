
import React from "react";

const HomePage = () => {
  return (
    <>
      <h1>Welcome to Your App</h1>

      <div className="debug">
        <div>API_URL: {process.env.REACT_APP_API_URL} </div>
      </div>
    </>
  );
};

export default HomePage;

