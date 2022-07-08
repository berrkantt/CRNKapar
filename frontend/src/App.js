import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {

  const handleSubmit = (e) => {
    e.preventDefault()
    const crn = e.target.crn.value;
    const token = e.target.token.value;
    console.log("İstenen CRN'ler: " + crn, "\n", "Token: " + token)
    axios.post("http://localhost:5000/api", { "crn": crn, "token": token })
  }


  return (


    <div>
      <header>ITU</header>
      <h1>Lavuklar Software Sunar...</h1>
      <h4>Since 1773</h4>

      <form onSubmit={handleSubmit}>
        <input type="text" name="crn" placeholder="crn" /><br></br><br></br>
        <input type="text" name="token" placeholder="token" /><br></br><br></br>
        <button>Kaydet</button>
      </form>
      <br></br><br></br>
      <br></br><br></br>

      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/0Kyl2WakR1w"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen></iframe>


      {" "}
    </div>
  );
}

export default App;
