import React from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

class FirstHomePage extends React.Component {
    constructor(props) {

        super(props);
        this.state = {
          
            keys:['C','%','Del','7','8','9','+','6','5','4','-','3','2','1','0','.','=']
        }
    }
    calc1(i,j){
      console.log(i,j)
      // alert(i,j)
    }

    render() { 
        return (
              
<div className="container-fluid" style={{backgroundColor:'green'}}>
  <div className="row">
    <div className="col-sm-2" >
      <h6><a href="#home" className="nav-link">HOME</a></h6>
      
    </div>
    <div className="col-sm-2">
      <h6><a href="#service" className="nav-link">SERVICE</a></h6>
    </div>
    <div className="col-sm-2">
      <h3><a href="#contact" className="nav-link">CONTACT US</a></h3>
    </div>
    <div className="col-sm-2">
      <h3><a href="#about" className="nav-link">ABOUT US</a></h3>
    </div>

        <div> 
            {
                this.state.keys.map((item, i)=>{
                    return (
                      <div key={i}>
                        <button onClick={ this.calc1(item, i)}>
                            {
                                item
                            }
                            </button>
                        </div>
                    )
                })
            }

        </div>
        </div>
        </div>


        );
    }
}
 
export default FirstHomePage;
// const style = {
//   background: '#282c34',
//   height: '100vh',
//   flex:'1',
//   flexdirection: 'column',
//   alignitems: 'center',
//   justifycontent: 'center',
//   fontsize: 'calc(10px + 2vmin)',
  
  
// }