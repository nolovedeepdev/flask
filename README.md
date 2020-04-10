# LABVIS template
<!DOCTYPE html>
  <html lang="pt-br">
    <link rel="shortcut icon" href="https://labvis-ufpa.github.io//favicon.png">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="">
      <meta name="author" content="">
      

      <title>Labvis</title>

      <!-- Bootstrap core CSS -->
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <!-- Custom styles for this template -->
      <link href="/static/css/modern-business.css" rel="stylesheet">
      <link href="/static/css/font-awesome.min.css" rel="stylesheet">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
      <style>
        /*custum from navbar*/
        .vertical-nav {
          min-width: 17rem;
          width: 17rem;
          height: 100vh;
          position: fixed;
          top: 0;
          left: 0;
          box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
          transition: all 0.4s;
        }
        .page-content {
          width: calc(100% - 17rem);
          margin-left: 17rem;
          transition: all 0.4s;
        }
        /* for toggle behavior */
        #sidebar.active {
          margin-left: -17rem;
        }
        #content.active { 
          width: 100%;
          margin: 0;
        }
        @media (max-width: 768px) {
          #sidebar {
            margin-left: -17rem;
          }
          #sidebar.active {
            margin-left: 0;
          }
          #content {
            width: 100%;
            margin: 0;
          }
          #content.active {
            margin-left: 17rem;
            width: calc(100% - 17rem);
          }
        }
        /*
        *
        * ==========================================
        * FOR DEMO PURPOSE
        * ==========================================
        *
        */
        body {
          background: #599fd9;
          background: -webkit-linear-gradient(to right, #599fd9, #c2e59c);
          background: linear-gradient(to right, #599fd9, #c2e59c);
          min-height: 100vh;
          overflow-x: hidden;
        }

        .separator {
          margin: 3rem 0;
          border-bottom: 1px dashed #fff;
        }
        .text-uppercase {
          letter-spacing: 0.1em;
        }
        .text-gray {
          color: #aaa;
        }
          
        /* Other styles for the page not related to the animated dropdown */
        
        /* css from back-to-top */
        .back-to-top {
        cursor: pointer;
        position: fixed;
        bottom: 20px;
        right: 20px;
        display:none;
        }

      </style>

      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/css/lightbox.min.css">
      <!--test-->
      <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    </head>

    <body>
      <!-- Vertical navbar -->

      <div class="vertical-nav bg-white" id="sidebar">
          <div class="py-4 px-3 mb-4 bg-light">
            <div class="media d-flex align-items-center"><img src="http://labvis.ufpa.br//images/logo.png" alt="..." width="65" class="mr-3 rounded-circle img-thumbnail shadow-sm">
              <div class="media-body">
                <h4 class="m-0">LABVIS</h4>
                <p class="font-weight-light text-muted mb-0">UFPa</p>
              </div>
            </div>
          </div>
        
          <p class="text-gray font-weight-bold text-uppercase px-3 small pb-4 mb-0">Main</p>
        
          <ul class="nav flex-column bg-white mb-0">
            <li class="nav-item">
              <a href="index" class="nav-link text-dark font-italic bg-light">
                  <svg class="bi bi-house-door-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path d="M6.5 10.995V14.5a.5.5 0 01-.5.5H2a.5.5 0 01-.5-.5v-7a.5.5 0 01.146-.354l6-6a.5.5 0 01.708 0l6 6a.5.5 0 01.146.354v7a.5.5 0 01-.5.5h-4a.5.5 0 01-.5-.5V11c0-.25-.25-.5-.5-.5H7c-.25 0-.5.25-.5.495z"/>
                      <path fill-rule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 01.5-.5h1a.5.5 0 01.5.5z" clip-rule="evenodd"/>
                    </svg>
                        Início
                    </a>
            </li>
            <li class="nav-item">
              <a href="about" class="nav-link text-dark font-italic">
                  <svg class="bi bi-folder-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M9.828 3h3.982a2 2 0 011.992 2.181l-.637 7A2 2 0 0113.174 14H2.826a2 2 0 01-1.991-1.819l-.637-7a1.99 1.99 0 01.342-1.31L.5 3a2 2 0 012-2h3.672a2 2 0 011.414.586l.828.828A2 2 0 009.828 3zm-8.322.12C1.72 3.042 1.95 3 2.19 3h5.396l-.707-.707A1 1 0 006.172 2H2.5a1 1 0 00-1 .981l.006.139z" clip-rule="evenodd"/>
                    </svg>
                        Sobre o projeto
                    </a>
            </li>
            <li class="nav-item">
              <a href="http://labvis.ufpa.br/" class="nav-link text-dark font-italic">
                  <svg class="bi bi-heart-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" clip-rule="evenodd"/>
                    </svg>
                        LABVIS
                    </a>
            </li>
            <li class="nav-item">
              <a href="https://github.com/nolovedeepdev/flask" class="nav-link text-dark font-italic">
                  <svg class="bi bi-building" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M15.285.089A.5.5 0 0115.5.5v15a.5.5 0 01-.5.5h-3a.5.5 0 01-.5-.5V14h-1v1.5a.5.5 0 01-.5.5H1a.5.5 0 01-.5-.5v-6a.5.5 0 01.418-.493l5.582-.93V3.5a.5.5 0 01.324-.468l8-3a.5.5 0 01.46.057zM7.5 3.846V8.5a.5.5 0 01-.418.493l-5.582.93V15h8v-1.5a.5.5 0 01.5-.5h2a.5.5 0 01.5.5V15h2V1.222l-7 2.624z" clip-rule="evenodd"/>
                      <path fill-rule="evenodd" d="M6.5 15.5v-7h1v7h-1z" clip-rule="evenodd"/>
                      <path d="M2.5 11h1v1h-1v-1zm2 0h1v1h-1v-1zm-2 2h1v1h-1v-1zm2 0h1v1h-1v-1zm6-10h1v1h-1V3zm2 0h1v1h-1V3zm-4 2h1v1h-1V5zm2 0h1v1h-1V5zm2 0h1v1h-1V5zm-2 2h1v1h-1V7zm2 0h1v1h-1V7zm-4 0h1v1h-1V7zm0 2h1v1h-1V9zm2 0h1v1h-1V9zm2 0h1v1h-1V9zm-4 2h1v1h-1v-1zm2 0h1v1h-1v-1zm2 0h1v1h-1v-1z"/>
                    </svg>
                        UFPa
                    </a>
            </li>
          </ul>
        
          <p class="text-gray font-weight-bold text-uppercase px-3 small py-4 mb-0">Charts</p>
        
            <li class="nav-item">
              <a class="nav-link text-dark font-italic" > 
                  <svg class="bi bi-bar-chart-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <rect width="4" height="5" x="1" y="10" rx="1"/>
                      <rect width="4" height="9" x="6" y="6" rx="1"/>
                      <rect width="4" height="14" x="11" y="1" rx="1"/>
                    </svg> 
                    <button class="btn btn-outline-light text-dark" type="button">Bar charts</button>
                    </a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-dark font-italic">
                  <svg class="bi bi-pie-chart" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M8 15A7 7 0 108 1a7 7 0 000 14zm0 1A8 8 0 108 0a8 8 0 000 16z" clip-rule="evenodd"/>
                      <path fill-rule="evenodd" d="M7.5 7.793V1h1v6.5H15v1H8.207l-4.853 4.854-.708-.708L7.5 7.793z" clip-rule="evenodd"/>
                    </svg>
                    <button class="btn btn-outline-light text-dark" type="button">Pie charts</button>
                    </a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-dark font-italic">
                  <svg class="bi bi-graph-up" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path d="M0 0h1v16H0V0zm1 15h15v1H1v-1z"/>
                      <path fill-rule="evenodd" d="M14.39 4.312L10.041 9.75 7 6.707l-3.646 3.647-.708-.708L7 5.293 9.959 8.25l3.65-4.563.781.624z" clip-rule="evenodd"/>
                      <path fill-rule="evenodd" d="M10 3.5a.5.5 0 01.5-.5h4a.5.5 0 01.5.5v4a.5.5 0 01-1 0V4h-3.5a.5.5 0 01-.5-.5z" clip-rule="evenodd"/>
                    </svg>
                    <button class="btn btn-outline-light text-dark" type="button">Scatter Plot</button>
                    </a>
            </li>
          </ul>
        </div>
        <!-- End vertical navbar -->

        <!-- Page content holder -->
        <div class="page-content p-5" id="content">
          <!-- Toggle button -->
        <button id="sidebarCollapse" type="button" class="btn btn-light bg-white rounded-pill shadow-sm px-4 mb-4"><small class="text-uppercase font-weight-bold">Toggle</small></button>
        
          <!-- End vertical navbar -->
        
        <!-- Page Content -->
        <div class="container"  id="pagina_retorno">

          <h1 class="my-4">Bem vindo ao projeto: Proposta e Avaliação de Templates de descrição Textual para vocalização de gráficos de barras</h1>
          <!-- Marketing Icons Section -->
            <div class="row">
              <div class="col-lg-4 mb-4">
                  <div class="card h-100">
                      <h4 class="card-header">Gráfico de Barras</h4>
                      <div class="card-body">
                          <p class="card-text">Apresentação dos gráficos de barra para interação.</p>
                      </div>
                      <div class="card-footer">
                        <a href ="bar" class="btn btn-primary">Abrir</a>
                    </div>
              </div>
            </div>
            <div class="col-lg-4 mb-4">
              <div class="card h-100">
                  <h4 class="card-header">Gráfico de Pizza</h4>
                  <div class="card-body">
                    <p class="card-text">Apresentação dos gráficos de pizza para interação.</p>
                    </div>
                  <div class="card-footer">
                      <a href="pie" class="btn btn-primary">Abrir</a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 mb-4">
              <div class="card h-100">
                <h4 class="card-header">Scatter Plot</h4>
                  <div class="card-body">
                    <p class="card-text">Apresentação dos gráficos scatter plot para interação.</p>
                      </div>
                    <div class="card-footer">
                            <a href="scatter" class="btn btn-primary">Abrir</a>
                        </div>
                    </div>
                </div>
            </div>
      <!-- /.row -->

      <!-- Portfolio Section -->
      
      <!-- init ajax -->
      <div id="box1"> 
        <div id="box2">
          <div id="box3">
        
            <header>
              <!--Gallery-->
              <h2>Prologal</h2>
              <div class="photo-gallery">
                  <div class="container">
                      <div class="intro">
                      </div>
                      <div class="row photos">
                          <div id="view" class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar0.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar0.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar1.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar1.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar2.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar2.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar3.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar3.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar4.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar4.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar5.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar5.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar6.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar6.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar7.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar7.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar8.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar8.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar9.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar9.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar10.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar10.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar11.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar11.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar12.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar12.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar13.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar13.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar14.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar14.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar15.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png/bar15.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie0.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie0.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie1.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie1.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie2.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie2.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie3.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie3.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie4.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie4.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie5.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie5.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie6.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie6.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie7.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie7.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie8.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie8.png?raw=true"></a></div>
                          <div class="col-sm-3 col-md-3 col-lg-3 item"><a href="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie9.png?raw=true" data-lightbox="photos"><img class="img-fluid img-thumbnail" src="https://github.com/nolovedeepdev/flask/blob/master/app/static/png-pie/pie9.png?raw=true"></a></div>
                          
                        </div>
                  </div>
              </div>

            <!--End gallery-->

            </header>

      <!-- end ajax -->
          </div>
        </div>
      </div>
      <div id="view"></div>
      <!-- Footer -->
      <p class="m-0 text-center text-white"> <br><strong>Copyright &copy; 2020, Universidade Federal Do Pará Laboratório de Visualização, Interação e Sistemas Inteligentes</strong></p>
    
      
      

    </body>
      <!-- Bootstrap core JavaScript -->
      <script type="text/javascript">
              var view;
          
              fetch('https://github.com/vega/vega/blob/master/docs/examples/barley-trellis-plot.vg.json')
                .then(res => res.json())
                .then(spec => render(spec))
                .catch(err => console.error(err));
          
              function render(spec) {
                view = new vega.View(vega.parse(spec), {
                  renderer:  'canvas',  // renderer (canvas or svg)
                  container: '#view',   // parent DOM container
                  hover:     true       // enable hover processing
                });
                return view.runAsync();
              }
            </script>
      <link src="/jquery/jquery.min.js">
      <link src="/jquery/jquery.js">
      <link src="app/static/jquery/jquery.slim.min.js">
      <link src="/jquery/bootstrap.bundle.min.js">
      <link src="/bootstrap/js/bootstrap.bundle.min.js">
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
      <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

      <!-- Core gallery-->
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/js/lightbox.min.js"></script>
      <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
      <script src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"></script>
      <script src="https://canvasjs.com/assets/script/jquery-ui.1.11.2.min.js"></script>
      <script src="https://canvasjs.com/assets/script/jquery.canvasjs.min.js"></script>
      <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
      
      <!--JS from navbar-->
      <script>
        $(function() {
          // Sidebar toggle behavior
          $('#sidebarCollapse').on('click', function() {
            $('#sidebar, #content').toggleClass('active');
          });
        });

      </script>

      <!-- Script from AJAX-->
      
      <script>
        $(document).ready(function(){
          $("button").click(function(){
            $("#box1").load("http://127.0.0.1:5000/api");
          });
        });
      </script>

</html>
