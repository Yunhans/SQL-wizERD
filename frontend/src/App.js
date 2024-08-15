import React, { useEffect, useState, useCallback } from 'react';
import { ReactFlow, MarkerType, MiniMap, Controls, Background, useNodesState, useEdgesState, applyNodeChanges, applyEdgeChanges, addEdge, Panel, ConnectionMode,} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import TableNode from './TableNode';
import SimpleFloatingEdge from './SimpleFloatingEdge';
import { LinkMarkers } from './Markers';

const proOptions = { hideAttribution: true };

const nodeTypes = {
	table: TableNode,
};

const edgeTypes = {
	floating: SimpleFloatingEdge,
};


const initialNodes = [
	{
		id: '1',
		type: 'table',
		data: {
			id: '1',
			label: 'Product',
			attribute: [
			{ name: 'product_id', type: 'int', isKey: true },
			{ name: 'quantity', type: 'int', isKey: false },
			{ name: 'product_type', type: 'char', isKey: false }
			]
		},
		position: { x: 0, y: 0 }
	},
	{
		id: '2',
		type: 'table',
		data: {
			id: '2',
			label: 'Order',
			attribute: [
			{ name: 'order_id', type: 'int', isKey: true },
			{ name: 'product_id', type: 'int', isKey: false },
			{ name: 'quantity', type: 'int', isKey: false }
			]
		},
		position: { x: 100, y: 100 }
	}
];

const initialEdges = [
	{ id: '1->2', source: '1', target: '2', markerStart: 'hasManyReversed',sourceHandle: 'a', targetHandle: 'b', label: '1-m', type: 'floating' },
];

const getNodeId = () => `randomnode_${+new Date()}`;

function App() {
	const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
	const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

	const onConnect = useCallback(
		(connection) => {
		  const edge = { ...connection, type: 'floating', markerStart: 'hasManyReversed' };
		  setEdges((eds) => addEdge(edge, eds));
		},
		[setEdges],
	  );

	const onAdd = useCallback(() => {
		const newNode = {
		  id: getNodeId(),
		  type: 'table',
		  data: {
			id: 'id',
			label: 'new Table',
			attribute:[
				{ name: 'id', type: 'INT', isKey: true }
			]
		   },
		  position: {
			x: (Math.random() - 0.5) * 400,
			y: (Math.random() - 0.5) * 400,
		  },
		};
		setNodes((nds) => nds.concat(newNode));
	}, [setNodes]);

	useEffect(() => {
		console.log('useEffect');
	
		function receiveMessage(e) {
			// console.log('Message received:', e);
			try {				
				const data = JSON.parse(e.data);
				// console.log('Iframe Data received:', data);

				if (data.task === 'allTables') {
					// Process the received data and update nodes or edges if needed
					try {
						setNodes(data.nodes);
						setEdges(data.edges);
					} catch (error) {
						console.error('Failed to parse or apply data:', error);
					}

				} 
				else if (data.task === 'specificTable') {
					console.log('Iframe Data received:', data.table_data);
					const table_data = data.table_data;
					document.getElementById('inputTableName').value = table_data.name;

					var attribute_html = '';
					table_data.attribute.forEach(function(value, index){
						attribute_html += '\
							<div class="row mb-2">\
								<div class="col-md-4">\
									<input type="text" class="form-control" id="inputAttrName-'+ index + '" value='+ value.name +'>\
								</div>\
								<div class="col-md-4">\
									<input class="form-control" list="datalistOptions" id="inputType-'+ index + '" value='+ value.type +'>\
									<datalist id="datalistOptions">\
										<option value="INT">\
										<option value="VARCHAR(255)">\
										<option value="DATE">\
									</datalist>\
								</div>\
								<div class="col-md-4 d-flex justify-content-around">\
									<!-- primary key -->\
									<input type="checkbox" class="btn-check" id="key-check-'+ index + '" autocomplete="off" '+ (value.primary_key? "checked" : "") +' >\
									<label class="btn btn-outline-warning" for="key-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="primary key">\
										<i class="bi bi-key-fill"></i>\
									</label>\
									<!-- notnull -->\
									<input type="checkbox" class="btn-check" id="null-check-'+ index + '" autocomplete="off" '+ (value.not_null? "checked" : "") +'>\
									<label class="btn btn-outline-danger" for="null-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="not null">\
										<i class="bi bi-ban"></i>\
									</label>\
									<!-- unique -->\
									<input type="checkbox" class="btn-check" id="uni-check-'+ index + '" autocomplete="off" '+ (value.unique? "checked" : "") +'>\
									<label class="btn btn-outline-dark" for="uni-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="unique">\
										<i class="bi bi-star-fill"></i>\
									</label>	\
									<!-- edit -->\
									<div class="btn-group">\
										<button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">\
											<i class="bi bi-three-dots"></i>\
										</button>\
										<div class="dropdown-menu" style="min-width: 250px;">\
											<p class="dropdown-header">Other Constraints</p>\
											<div class="form-check mx-3 mb-2">\
												<input class="form-check-input" type="checkbox" value="" id="auto-check-'+ index + '"  >\
												<label class="form-check-label" for="auto-check-'+ index + '">\
													auto increment\
												</label>\
											</div>\
											<div class="mx-3">\
												<label for="default-'+ index + '" class="form-label mb-0">default</label>\
												<input type="text" class="form-control form-control-sm" id="default-'+ index + '">\
											</div>\
											<div class="dropdown-divider"></div>\
											<p class="dropdown-header">Actions</p>\
											<button type="button" class="btn btn-sm btn-danger mx-3 mb-2"><i class="bi bi-trash3"></i> Delete attribute</button>\
										</div>\
									</div>\
								</div>\
							</div>\
						';	
					});

					document.getElementById('attribute-container').innerHTML = attribute_html;
				}				

			} catch (error) {
				console.error('Failed to parse data:', e.data);
			}
		}
	
		// console.log('Setting up message listener');
		window.addEventListener('message', receiveMessage, false);
	
		return () => {
			// console.log('Cleaning up message listener');
			window.removeEventListener('message', receiveMessage);
		};
	}, []);

	return (
		<div style={{ height: '100%', width: '100%'}}>
			<LinkMarkers />
			<ReactFlow
				nodes={nodes}
				onNodesChange={onNodesChange}
				edges={edges}
				onEdgesChange={onEdgesChange}
				onConnect={onConnect}
				fitView
				minZoom={0.2}
				edgeTypes={edgeTypes}
				nodeTypes={nodeTypes}
				proOptions={proOptions}
        		connectionMode={ConnectionMode.Loose}
			>
				<Panel position="bottom-center">
					<button type="button" className="btn btn-success" onClick={onAdd}>add Table</button>
				</Panel>
				<Background />
				<Controls position = 'bottom-right' showInteractive={false}/>
				<MiniMap position='top-right' nodeStrokeWidth={3} />
			</ReactFlow>
		</div>
	);
}

export default App;

