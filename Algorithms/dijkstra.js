class Vertex {
  constructor(id) {
    this.id = id;
    this.neighbors = [];
    this.dist = Infinity;
    this.prev = undefined;
  }

  addNeighbor(id, weight) {
    this.neighbors.push({
      id,
      weight,
    });
  }

  getWeight(id) {
    return this.neighbors.find(vertex => vertex.id === id).weight;
  }

  reset() {
    this.dist = Infinity;
    this.prev = undefined;
  }
}

class Graph {
  constructor() {
    this.vertices = [];
    this.lastId = 0;
  }

  addVertex() {
    const vertex = new Vertex(this.lastId);
    this.vertices.push(vertex);
    this.lastId = this.lastId + 1;

    return vertex;
  }

  addConnection(source, target, weight) {
    this.vertices.find(vertex => vertex.id === source).addNeighbor(target, weight);
  }

  getVertex(id) {
    return this.vertices.find(vertex => vertex.id === id);
  }

  reset() {
    for (const vertex of this.vertices) {
      vertex.reset();
    }
  }
}

const graph = new Graph();

const a = graph.addVertex();
const b = graph.addVertex();
const c = graph.addVertex();
const d = graph.addVertex();
const e = graph.addVertex();
const f = graph.addVertex();

graph.addConnection(a.id, b.id, 7);
graph.addConnection(a.id, c.id, 9);
graph.addConnection(a.id, f.id, 14);
graph.addConnection(b.id, c.id, 10);
graph.addConnection(b.id, d.id, 15);
graph.addConnection(b.id, a.id, 7);
graph.addConnection(c.id, d.id, 11);
graph.addConnection(c.id, f.id, 2);
graph.addConnection(c.id, a.id, 9);
graph.addConnection(c.id, b.id, 10);
graph.addConnection(d.id, b.id, 15);
graph.addConnection(d.id, c.id, 11);
graph.addConnection(e.id, f.id, 9);
graph.addConnection(e.id, d.id, 6);
graph.addConnection(f.id, e.id, 9);
graph.addConnection(f.id, c.id, 2);
graph.addConnection(f.id, a.id, 14);

function dijkstra(graph, source, target) { // eslint-disable-line
  // create queue
  const queue = graph.vertices.slice().map(i => i.id);
  // initalizing
  graph.reset();
  graph.getVertex(source).dist = 0; // eslint-disable-line
  // algorithm
  while (queue.length) {
    // find a vertex that has min dist
    let u = graph.getVertex(graph.vertices
      .filter(i => queue.includes(i.id))
      .sort((first, second) => first.dist - second.dist)[0].id);
    // find target
    if (u.id === target) {
      const result = [];
      if (u.prev || u.id === source) {
        while (u) {
          result.unshift(u);
          u = u.prev;
        }
      }
      return result;
    }
    // remove u from queue
    {
      const index = queue.indexOf(u.id);
      queue.splice(index, 1);
    }

    for (const v of u.neighbors) {
      if (queue.includes(v.id)) {
        const alt = u.dist + v.weight;
        const orgV = graph.getVertex(v.id);
        if (alt < orgV.dist) {
          orgV.dist = alt;
          orgV.prev = u;
        }
      }
    }
  }
}

dijkstra(graph, 0, 4);

// console.log(dijkstra(graph, 0, 4));
