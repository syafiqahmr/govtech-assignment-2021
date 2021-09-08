import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./Components/Home";
import Link from "./Components/Link";

function App() {
  return (
    <div className="app">
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/:shortUrl" component={Link} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
