<template>
  <div>
    <div>
        <HeaderNav></HeaderNav>
        <div>
            <Sidebar></Sidebar>
            <div class="center-main">
                <P class="center-title" type="danger" icon="el-icon-delete">Your collection</P>
                <el-form ref="form" :model="form" label-width="80px">


                  <div class="divcss5" :span="8">

                     <el-row>


<!--111-->
                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>

<!--                       222-->
                     <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>


<!--                       333-->
                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>


                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>



                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>



                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>



                       <el-col :span="6" >
                         <div>
                       <div id="div2">
                      <el-card :body-style="{ padding: '0px' }" >
<!--                      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">-->

                        <div id="content2">
                        <article class="post-152 post type-post status-publish format-standard hentry category-people category-photos">
                        <div class="post-format-content">
                        <div class="post-thumbnail">
                          <img width="280" height="280" src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" class="attachment-thumbnail wp-post-image" alt="105694702">
                        </div>
                        <div class="content-wrap">
                        <h1 class="entry-title"><a href="" class="featured-image" title="amp; Fashion" rel="bookmark">
                          <div>Seller：liangbj0405</div>
                          <br>
                          <div>Date：2020.1.1</div>
                          <br>
                          <div>Current price：200W</div>
                        </a></h1>

                        </div>


                        </div>
                        </article>
                        </div>

                      <div style="padding: 0px;">
                      <ul id="divcss4"><li><a href="#">[Taoran North Shore] North and South facing three rooms and one hall, fine decoration with furniture</a></li></ul>
                      <div class="bottom clearfix">
                      <el-dropdown>
                      <el-button type="primary" icon="el-icon-s-tools">
                        Option<i class="el-icon-arrow-down el-icon--right"></i>
                      </el-button>
                      <el-dropdown-menu slot="dropdown">
<!--                        <el-button type="primary" icon="el-icon-search">搜索</el-button>-->
                        <el-dropdown-item>Detail</el-dropdown-item>
                        <el-dropdown-item v-on:click="deldiv">Delete</el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>

                      </div>
                      </div>
                      </el-card>
                          </div>
                           </div>
                         </el-col>






                      </el-row>






                   </div>


                    <el-divider></el-divider>

                    <el-divider></el-divider>



                    <el-form-item  style="text-align: right">
                        <el-button type="primary" @click="onSubmit" size="medium">S a v e</el-button>
<!--                        <el-button>取消</el-button>-->
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
name: "collection",
methods: {
          deldiv:function () {
         var obj=document.getElementById('div2');
         obj.parentNode.removeChild(obj);
      }
    },
    maijia:'liangbj0405'
}

// function deldiv(){
//   var obj=document.getElementById('div2');
//   obj.parentNode.removeChild(obj);
// }
</script>

<style scoped>


/*超出省略*/
/**{ padding:0; margin:0}*/
/*    a{ text-decoration:none;color:#6699ff}*/
/*    ul,li{ list-style:none; text-align:left}*/

    #divcss4{padding:10px; width:240px;
     margin-top:10px}
    #divcss4 li{width:250px;height:24px;line-height:24px; font-size:14px;
    color:#6699ff;overflow:hidden;text-overflow:ellipsis;
    /*border-bottom:1px #ff8000 dashed;*/
    }
    #divcss4 li a:hover{ color:#333}














#content article {
float: left;
margin-right: 4%;
max-width: 236px;
position: relative;
width: 22%;
margin-bottom: 3.5%;
}
#content article:nth-child(4n+4) {
margin-right: 0;
}
.post-format-content {
position: relative;
background: #111;
}
.post-thumbnail {
max-width: 100%;
height: auto;
overflow: hidden;
}
.content-wrap {
padding: 0;
position: absolute;
text-align: center;
width: 100%;
top: 0;
bottom: 0;
display: table-cell;
vertical-align: middle;
overflow: hidden;
}
.content-wrap h1.entry-title {
display: table;
font-size: 110%;
height: 100%;
text-transform: uppercase;
width: 100%;
margin:0;
}

.content-wrap h2.entry-title {
display: table;
font-size: 110%;
height: 100%;
text-transform: uppercase;
width: 100%;
margin:0;
}
.edit-link {
z-index: 2;
}
.featured-image {
display: table-cell;
position: relative;
transition: opacity .25s ease-in-out, background .25s ease-in-out;
-moz-transition: opacity .25s ease-in-out, background .25s ease-in-out;
-webkit-transition: opacity .25s ease-in-out, background .25s ease-in-out;
vertical-align: middle;
z-index: 1;
color: #fff;
text-decoration: none;
opacity: 0;
padding: 10%;
}
.featured-image:hover {
opacity: 0.9;
color: #fff;
background: rgba(0,0,0,0.8);
}
.post-thumbnail img {
display: block;
}
img {
max-width: 100%;
height: auto;
}




    #div1, #div2, #div3{
        display: inline-block;
    }

.divcss5{
  /*border:3px solid #AAAAAA;*/
  width:1500px;
	height:1160px;
	/*transition:width 2s;*/
	/*-webkit-transition:width 2s; !* Safari *!*/

}

.el-dropdown {
    vertical-align: top;
  }
  .el-dropdown + .el-dropdown {
    margin-left: 15px;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }


.time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }



  /*效果css*/
    *, *:after, *:before { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; }
    a {
	color: #888;
	text-decoration: none;
}
a:hover, a:active {
	color: #333;
}

.grid {
	padding: 20px 20px 100px 20px;
	max-width: 1300px;
	margin: 0 auto;
	list-style: none;
	text-align: center;
}

.grid li {
	display: inline-block;
	width: 440px;
	margin: 0;
	padding: 20px;
	text-align: left;
	position: relative;
}

.grid figure {
	margin: 0;
	position: relative;
}

.grid figure img {
	max-width: 100%;
	display: block;
	position: relative;
}

.grid figcaption {
	position: absolute;
	top: 0;
	left: 0;
	padding: 20px;
	background: #2c3f52;
	color: #ed4e6e;
}

.grid figcaption h3 {
	margin: 0;
	padding: 0;
	color: #fff;
}

.grid figcaption span:before {
	content: 'by ';
}

.grid figcaption a {
	text-align: center;
	padding: 5px 10px;
	border-radius: 2px;
	display: inline-block;
	background: #ed4e6e;
	color: #fff;
}

/* 说明文字样式 5 */

.cs-style-5 figure img {
	z-index: 10;
	-webkit-transition: -webkit-transform 0.4s;
	-moz-transition: -moz-transform 0.4s;
	transition: transform 0.4s;
}

.no-touch .cs-style-5 figure:hover img,
.cs-style-5 figure.cs-hover img {
	-webkit-transform: scale(0.4);
	-moz-transform: scale(0.4);
	-ms-transform: scale(0.4);
	transform: scale(0.4);
}

.cs-style-5 figcaption {
	height: 100%;
	width: 100%;
	opacity: 0;
	-webkit-transform: scale(0.7);
	-moz-transform: scale(0.7);
	-ms-transform: scale(0.7);
	transform: scale(0.7);
	-webkit-backface-visibility: hidden;
	-moz-backface-visibility: hidden;
	backface-visibility: hidden;
	-webkit-transition: -webkit-transform 0.4s, opacity 0.4s;
	-moz-transition: -moz-transform 0.4s, opacity 0.4s;
	transition: transform 0.4s, opacity 0.4s;
}

.no-touch .cs-style-5 figure:hover figcaption,
.cs-style-5 figure.cs-hover figcaption {
	-webkit-transform: scale(1);
	-moz-transform: scale(1);
	-ms-transform: scale(1);
	transform: scale(1);
	opacity: 1;
}

.cs-style-5 figure a {
	position: absolute;
	bottom: 20px;
	right: 20px;
}


/* Chrome, Safari, Opera */
@-webkit-keyframes mymove {
    50% {background-color: #00FFFF;}
}

/* Standard syntax */
/*@keyframes mymove {*/
/*    50% {background-color: blue;}*/
/*}*/





    .center-main{
        height: 100%;
        width: calc(80% - 65px);
        margin: 0 10% 0 calc(10% + 65px);
    }
    .center-title{
        font-size: 2rem;
        padding: 30px;
        text-align: right;
        position: relative;
        overflow: hidden;
    }
    .center-title:after {
        content: "";
        display: block;
        position: absolute;
        bottom: 10%;
        left: 0;
        height: 5px;
        width: 200%;
        background-color: #caa;
        background-image: linear-gradient(to right, #cc7575, #ffd544 50%, #cc7575);
        animation:colorLine 1s alternate infinite;
    }



    .fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}







    .box {
		height: 80%;
		/*overflow-y: auto;*/
		display: flex;
		flex-direction: column;
	}
    .el-card{
		margin-bottom:20px;
	}


    @keyframes colorLine
    {
        from {left:-100%;}
        to {left: 0}
    }
</style>