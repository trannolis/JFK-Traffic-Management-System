import './App.css';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Landing from './pages/landing';


export default function App() {
  return (
     <Router>
       <div>
         <nav>
           <ul>
             <li>
               <Link to="/">Landing</Link>
             </li>
           </ul>
         </nav>

         {/* A <Switch> looks through its children <Route>s and
             renders the first one that matches the current URL. */}
         <Switch>
           <Route path="/">
             <Landing />
           </Route>
         </Switch>
       </div>
     </Router>
   );
 }
