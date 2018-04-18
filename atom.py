def plot_atom(fl):
    f = open('try.html','w')

    # fl = "reviews.csv"

    message = """<!doctype html>
<meta charset="utf-8">
<html>
<head>
    <style>
        .maincircle {
            fill: #ccff33;
            /*stroke: black;*/
            /*opacity:0.5;*/
            stroke-width: 1;
        }
        .good {
            fill: green;
        }
        .bad {
            fill: black;
        }
    </style>
    <script src="https://d3js.org/d3.v4.min.js"></script>
</head>
<body>
<svg width="1440" height="900"></svg>
<script>

    var svg = d3.select("svg"),
            margin = 200,
            width = svg.attr("width") - margin,
            height = svg.attr("height") - margin
            r0 = 50,
            x0=width/2,
            y0=height/2;

   var g = svg.append("g")
           .attr("id" , "c1")
           .attr("transform", "translate(" + 100 + "," + 100 + ")");

   var bigcircle = g.append("circle")
                    .attr("class","maincircle")
                    .attr("cx",x0)
                    .attr("cy",y0)
                    .attr("r",r0);

        g.append("text")
                 .attr("x", width/2-32)
                 .attr("y", height/2+10)
                 .attr("font-size", "30px")
                 .attr("fill" , "black")
                 .attr("font-family","sans-serif")
                 .attr("font-weight","900")
                 .text("OLA");

    d3.csv('"""+fl+"""', function(error, data) {
        if (error) throw error;

        var dis = [];
        var count=0,mn=100000,mx=0,mid;

        data.forEach(function(d,i) {
            dis[i]= r0 + Math.floor(100*d.reviewStrength);
            //dis[i] = dis[i] + dis[i]*1;
            dis[i] = dis[i] + Math.pow(2,dis[i]/20);
            count++;
            mn=Math.min(mn,dis[i]);
            mx=Math.max(mx,dis[i]);
            //console.log(dis[i]);
        });

        mid = r0+50;
        mid = mid + Math.pow(2,mid/20);

        dis.sort(function(a,b){
            return d3.ascending(+a,+b);
        });

        var clrsc = d3.scaleLinear()
        .domain([mn,mx*0.6])
        .range(["green","red"]);

        var x1=[];
        var y1,r1;

        g.selectAll(".bad")
         .data(dis)
         .enter().append("circle")
         .attr("fill", function(d,i){
            d = Math.floor(d);
            return clrsc(d);
         })
         .attr("cx", function(d,i){
             x1[i]=Math.random()*2*(d)+(x0-d);
             return x1[i];
          })
         .attr("cy", function(d,i) {
             r1=d;
             y1 = (r1*r1) - ((x1[i]-x0)*(x1[i]-x0));
             y1 = Math.floor(Math.sqrt(y1));

             if(i%2 == 0)
             y1 = y0 + y1;
             else
             y1 = y0 - y1;
             //console.log(y1);
             return y1;
         })
         .attr("r", function(d,i){
             return d/70;
         });

    });


</script>
</body>
</html>

    """

    f.write(message)
    f.close()
