import { Component } from 'react';

class Link extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shortUrl: "",
      hideError: true,
      api: process.env.REACT_APP_API_URL
    }
  }

  componentDidMount() {
    this.setState({
      shortUrl: this.props.match.params.shortUrl
    }, () => this.getData())
  }



  getData() {
    var url = this.state.api + "/" + this.state.shortUrl

    fetch(url).then(res => res.json()).then(
      (data) => {
        if (data == null) {
          this.setState({
            hideError: false
          })
        } else {
          window.location.href = data.long_url;
        }
      },
      (error) => {
        console.log(error);
      }
    )
  }


  render() {
    return (
      <div>
        {!this.state.hideError ?
          <div className="w-screen h-screen bg-gray-100">
            <div className="flex flex-wrap content-center max-w-2xl justify-center mx-auto my-auto px-2">
              <div className="w-full my-4 block h-full">
                <h1 className="text-3xl font-bold text-center my-2">Invalid Short URL</h1>
                <p className="text-indigo-600 text-lg font-medium text-center hover:text-indigo-400">
                  <a href="/" >Back to Home</a>
                </p>
              </div>
            </div>
          </div>
          :
          <div className="w-screen h-screen bg-gray-100">
            <div className="flex flex-wrap content-center max-w-2xl justify-center mx-auto my-auto px-2">
              <div className="w-full my-4 block h-full">
                <h1 className="text-3xl font-bold text-center my-2">Redirecting...</h1>
              </div>
            </div>
          </div>
        }
      </div>
    );
  }
}

export default Link;