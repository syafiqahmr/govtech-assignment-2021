import './App.css';
import { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      longUrlForm: "wdke",
      longUrl: "lewmd",
      shortUrl: "wed",
      hideResultSuccess: true,
      api: "https://localhost:8000/url"
    }
  }

  postData() {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ long_url: this.state.longUrl })
    };

    fetch(this.state.api, requestOptions).then(res => res.json).then(
      (result) => {
        this.setState({
          hideResultSuccess: false,
          longUrl: result.long_url,
          shortUrl: result.short_url
        });
      },
      (error) => {
        console.log(error);
      }
    )
  }


  render() {
    return (
      <div className="App" >
        <div className="w-screen h-screen bg-gray-100">
          <div className="flex flex-wrap content-center max-w-2xl justify-center mx-auto px-2">
            <div className="w-full my-4 block">
              <h1 className="text-3xl font-bold text-center my-2">Url Shorterner</h1>
              <h3>Enter a long URL to make a short URL!</h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-6 w-full gap-y-4 sm:gap-x-4 border-b-2 border-gray-200 pb-8">
              <input
                type="text"
                value={this.state.longUrlForm}
                className="col-span-5 mt-1 h-10 rounded-md border-gray-300 shadow-sm focus:border-indigo-200 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                placeholder="Your Long URL"
              />
              <button
                className="w-24 justify-self-end sm:w-full mt-1 block h-10 rounded-md bg-indigo-200 font-medium"
              >
                Submit
              </button>
            </div>

            <div className="grid grid-cols-1 gap-y-4 mt-6 w-full">
              <h2 className="text-2xl font-bold text-center my-2">Shorten Success</h2>
              <label className="block">
                <span className="text-gray-700">Your long URL</span>
                <input
                  type="text"
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                  value={this.state.longUrl}
                  readOnly
                />
              </label>
              <label className="block">
                <span className="text-left">Your short URL</span>
                <input
                  type="text"
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                  placeholder=""
                  value={this.state.shortUrl}
                  readOnly
                />
              </label>
            </div>
          </div>

        </div>
      </div>
    );
  }
}

export default App;
