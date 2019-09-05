function directionalDot() {
    const margin = {
        top: 48,
        right: 16,
        bottom: 66,
        left: 96
    };
    let width = 0;
    let height = 0;
    const chart = d3.select('.chart-sueldos');
    const svg = chart.select('svg');
    const scales = {};
    let dataz;
    let symbolP = '€';
    const setupScales = () => {
        const countX = d3.scaleLinear().domain([0, d3.max(dataz, (d) => d.max * 1.05)]);

        const countY = d3.scaleBand().domain(dataz.map((d) => d.CCAA));

        scales.count = { x: countX, y: countY };
    };

    const setupElements = () => {
        const g = svg.select('.chart-sueldos-container');

        g.append('g').attr('class', 'axis axis-x');

        g.append('g').attr('class', 'axis axis-y');

        g.append('g').attr('class', 'chart-sueldos-container-bis');
    };

    const updateScales = (width, height) => {
        scales.count.x.range([0, width]);
        scales.count.y.range([0, height]);
    };

    const drawAxes = (g) => {
        const axisX = d3
            .axisTop(scales.count.x)
            .tickPadding(15)
            .tickFormat((d) => d + symbolP)
            .ticks(11)
            .tickSizeInner(height);

        g.select('.axis-x')
            .attr('transform', `translate(0,${height})`)
            .transition()
            .duration(500)
            .ease(d3.easeLinear)
            .call(axisX);

        const axisY = d3
            .axisLeft(scales.count.y)
            .tickPadding(5)
            .tickFormat((d) => d)
            .ticks(15)
            .tickSizeInner(-width);

        g.select('.axis-y')
            .transition()
            .duration(500)
            .ease(d3.easeLinear)
            .call(axisY);
    };

    const updateChart = (dataz) => {
        const w = chart.node().offsetWidth;
        const h = 600;

        width = w - margin.left - margin.right;
        height = h - margin.top - margin.bottom;

        svg.attr('width', w).attr('height', h);

        const translate = `translate(${margin.left},${margin.top})`;

        const g = svg.select('.chart-sueldos-container');

        g.attr('transform', translate);

        updateScales(width, height);

        const container = chart.select('.chart-sueldos-container-bis');

        const layer = container.selectAll('.circle-max').data(dataz);

        layer.exit().remove();

        const layerDos = container.selectAll('.circle-min').data(dataz);

        layerDos.exit().remove();

        const layerTres = container.selectAll('.circle-mean').data(dataz);

        layerTres.exit().remove();

        const newLayer = layer
            .enter()
            .append('circle')
            .attr('class', 'circle-max');

        const newLayerDos = layerDos
            .enter()
            .append('circle')
            .attr('class', 'circle-min');

        const newLayerTres = layerTres
            .enter()
            .append('circle')
            .attr('class', 'circle-mean');

        layer
            .merge(newLayer)
            .transition()
            .duration(500)
            .ease(d3.easeLinear)
            .attr('r', 6)
            .attr('cy', (d) => scales.count.y(d.CCAA) + 15.5)
            .attr('cx', (d) => scales.count.x(d.max));

        layerDos
            .merge(newLayerDos)
            .transition()
            .duration(500)
            .ease(d3.easeLinear)
            .attr('r', 6)
            .attr('cy', (d) => scales.count.y(d.CCAA) + 15.5)
            .attr('cx', (d) => scales.count.x(d.min));

        layerTres
            .merge(newLayerTres)
            .transition()
            .duration(500)
            .ease(d3.easeLinear)
            .attr('r', 6)
            .attr('cy', (d) => scales.count.y(d.CCAA) + 15.5)
            .attr('cx', (d) => scales.count.x(d.mean));

        const legend = svg
            .selectAll('.label')
            .data(dataz)
            .enter()
            .append('g')
            .attr('class', (d) => d.labels + ' container-labels')
            .on('click', (d) => {
                const active = d.active !== true;
                const newRadius = active ? 0 : 6;
                d3.selectAll(`.circle-${d.labels}`)
                    .transition()
                    .duration(300)
                    .ease(d3.easeLinear)
                    .style('r', newRadius);
                d.active = active;
            })
            .attr('transform', (d, i) => `translate(${i * 100},${height})`);

        legend
            .append('circle')
            .attr('cx', margin.left + 20)
            .attr('cy', margin.left)
            .attr('r', 8)
            .attr('class', 'legend-rect');

        legend
            .append('text')
            .attr('class', 'legend-text')
            .attr('x', margin.left + 40)
            .attr('y', margin.left)
            .attr('dy', '.35em')
            .text((d) => d.labels);

        drawAxes(g);
    };

    const resize = () => {
        updateChart(dataz);
    };

    const loadData = () => {
        d3.csv('csv/max-min-mean.csv', (error, data) => {
            if (error) {
                console.log(error);
            } else {
                dataz = data;
                dataz.forEach((d) => {
                    d.max = +d.max;
                    d.min = +d.min;
                    d.mean = +d.mean;
                });
                console.log(dataz);
                setupElements();
                setupScales();
                updateChart(dataz);
            }
        });
    };

    window.addEventListener('resize', resize);

    loadData();
}

directionalDot();
