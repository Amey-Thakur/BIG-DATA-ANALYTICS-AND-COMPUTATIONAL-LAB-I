// Neo4j Graph Database - Car Database
// Author: Amey Thakur (https://github.com/Amey-Thakur)
// Course: Big Data Analytics & Computational Lab -I (BDA&CL-I)
// Experiment 4: Study and Run NoSQL Programs (Neo4j)
// Date: October 10, 2021

// ========================================
// CREATE CAR NODES
// ========================================

// SubCompact Cars
CREATE (n:Car{name:'Chevrolet Bolt',type:'SubCompact', color:'Red',fuel:'Petrol'})
CREATE (n:Car{name:'Kia Rio',type:'SubCompact', color:'Blue',fuel:'Diesel'})
CREATE (n:Car{name:'Toyota Yaris',type:'SubCompact', color:'Black',fuel:'CNG'})
CREATE (n:Car{name:'Mini Cooper',type:'SubCompact', color:'White',fuel:'Diesel'})

// Compact Cars
CREATE (n:Car{name:'Toyota Corolla',type:'Compact', color:'Black',fuel:'CNG'})
CREATE (n:Car{name:'Volkswagen Golf',type:'Compact', color:'White',fuel:'Petrol'})
CREATE (n:Car{name:'Honda Fit',type:'Compact', color:'Blue',fuel:'Diesel'})
CREATE (n:Car{name:'Mazda 3',type:'Compact', color:'Red',fuel:'Electric'})

// Sedan Cars
CREATE (n:Car{name:'BMW 320i',type:'Sedan', color:'Black',fuel:'Electric'})
CREATE (n:Car{name:'Volkswagen Arteon',type:'Sedan', color:'Red',fuel:'Diesel'})
CREATE (n:Car{name:'Mercedes-Benz C 300',type:'Sedan', color:'Blue',fuel:'Petrol'})
CREATE (n:Car{name:'KIA Stinger',type:'Sedan', color:'White',fuel:'Electric'})

// Luxury Cars
CREATE (n:Car{name:'Audi A8',type:'Luxury', color:'Green',fuel:'Petrol'})
CREATE (n:Car{name:'Rolls-Royce Phantom',type:'Luxury', color:'Black',fuel:'Electric'})
CREATE (n:Car{name:'Bently Bentayga',type:'Luxury', color:'Black',fuel:'Petrol'})
CREATE (n:Car{name:'Mercedes-Benz S 550',type:'Luxury', color:'Red',fuel:'Electric'})

// ========================================
// CREATE AFFORDABILITY NODES
// ========================================

CREATE (n:affordability{name:'Lavish', cost:'500$'})
CREATE (n:affordability{name:'Economic', cost:'250$'})

// ========================================
// CREATE COMPANY NODES
// ========================================

CREATE (n:Company{name:'Toyota'})
CREATE (n:Company{name:'Mercedes'})

// ========================================
// CREATE SPECIAL OFFER NODES
// ========================================

CREATE (n:Special{name:'BEST DEAL'})
CREATE (n:Special{name:'20% Discount'})

// ========================================
// CREATE RELATIONSHIPS
// ========================================

// Match Affordability to Cars
MATCH (a:affordability), (c:Car)
WHERE a.name = 'Lavish' AND c.name='Mini Cooper'
CREATE (c)-[aff:BUDGET]->(a)

MATCH (a:affordability), (c:Car)
WHERE a.name = 'Economic'
CREATE (c)-[aff:BUDGET]->(a)

// Match Company to Cars
MATCH (p:Company), (c:Car)
WHERE p.name = 'Mercedes' AND c.name='Mercedes-Benz C 300'
CREATE (c)-[same:Parent_Company]->(p)

MATCH (p:Company), (c:Car)
WHERE p.name = 'Mercedes' AND c.name='Mercedes-Benz S 550'
CREATE (c)-[same:Parent_Company]->(p)

MATCH (p:Company), (c:Car)
WHERE p.name = 'Toyota'
CREATE (c)-[same:Parent_Company]->(p)

// Match Special Offers to Cars
MATCH (s:special), (c:Car)
WHERE s.name = '20% Discount' AND c.name='Honda Fit'
CREATE (c)-[deal:OFFER]->(p)

MATCH (s:special), (c:Car)
WHERE s.name = 'BEST DEAL'
CREATE (c)-[deal:OFFER]->(p)

// ========================================
// QUERY EXAMPLES
// ========================================

// List all car nodes
// MATCH (n:Car) RETURN n

// Find cars by type
// MATCH (n:Car) WHERE n.type = 'Luxury' RETURN n

// Find cars with special offers
// MATCH (c:Car)-[:OFFER]->(s:Special) RETURN c, s

// Find cars by company
// MATCH (c:Car)-[:Parent_Company]->(p:Company) WHERE p.name = 'Mercedes' RETURN c

// Find cars by affordability
// MATCH (c:Car)-[:BUDGET]->(a:affordability) WHERE a.name = 'Economic' RETURN c
