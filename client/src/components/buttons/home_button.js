import react from 'react';
import { Fab } from '@material-ui/core';


const HomeButton = () => {

    const styles = {
        color: 'white',
        textDecoration: 'none',
        marginLeft: '10vw'
    }
    return (
        <a href='/' style={styles}>
            <h1> JFK ATMS </h1>
        </a>
    )
}

export default HomeButton
