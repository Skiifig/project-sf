<style>
        .container {
          padding: 20px;
        }
        button,
        button::after {
          -webkit-transition: all 0.3s;
          -moz-transition: all 0.3s;
          -o-transition: all 0.3s;
          transition: all 0.3s;
        }
        button {
          background: none;
          border: 3px solid rgb(0, 0, 0);
          border-radius: 10px;
          color: rgb(0, 0, 0);
          display: block;
          font-size: 1em;
          font-weight: bold;
          margin: 10px auto;
          padding: 1em 2em;
          position: relative;
          text-transform: uppercase;
        }
        button::before,
        button::after {
          background: rgb(11, 133, 221);
          content: "";
          position: absolute;
          z-index: -1;
        }
        button:hover {
          color: #000000;
        }
        .button1::after {
          height: 0;
          left: 0;
          top: 0;
          width: 100%;
        }
        .button1:hover:after {
          height: 100%;
        }
</style>