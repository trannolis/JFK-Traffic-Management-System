import react from 'react';

import { Fab } from '@material-ui/core';
import Home_button from "../components/buttons/home_button";

const homePilot = () => {
  const styles = {
    display: 'flex',
    flexDirection: 'column',
    marginTop: '20vh',
    alignItems: 'center'
  }

  const home_style = {
    margin: '2vw'
  }

  return (
      <div style = {home_style}>
        <Home_button/>
      <div style = {styles}>
      <h1> Landing and Takeoff Information Displayed Here </h1>
      </div>
      </div>
  )
};

export default homePilot
