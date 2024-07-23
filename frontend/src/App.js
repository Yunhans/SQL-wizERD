import React, { useEffect, useState, useCallback } from 'react';
import ReactFlow, { Controls, Background, applyNodeChanges, applyEdgeChanges, addEdge, Panel,} from 'reactflow';
import 'reactflow/dist/style.css';
import TableNode from './TableNode';

const proOptions = { hideAttribution: true };

const nodeTypes = {
	table: TableNode,
};

const initialNodes = [
	{
		id: '1',
		"type": 'table',
		data: {
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
	{ id: '1->2', source: '1', target: '2', label: '1-m', type: 'smoothstep' },
];

const getNodeId = () => `randomnode_${+new Date()}`;

function App() {
	const [nodes, setNodes] = useState(initialNodes);
	const [edges, setEdges] = useState(initialEdges);

	const onNodesChange = useCallback(
		(changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
		[],
	);
	const onEdgesChange = useCallback(
		(changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
		[],
	);

	const onConnect = useCallback(
		(params) => setEdges((eds) => addEdge(params, eds)),
		[],
	);

	const onAdd = useCallback(() => {
		const newNode = {
		  id: getNodeId(),
		  type: 'table',
		  data: { 
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
				console.log('Data received:', data);
	
				// Process the received data and update nodes or edges if needed
				try {
					setNodes(data.nodes);
                    setEdges(data.edges);
				} catch (error) {
					console.error('Failed to parse or apply data:', error);
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
			<ReactFlow
				nodes={nodes}
				onNodesChange={onNodesChange}
				edges={edges}
				onEdgesChange={onEdgesChange}
				onConnect={onConnect}
				fitView
				nodeTypes={nodeTypes}
				proOptions={proOptions}
			>
				<Panel position="bottom-center">
					<button type="button" className="btn btn-success" onClick={onAdd}>add Table</button>
				</Panel>
				<Background />
				<Controls position = 'bottom-right'/>
			</ReactFlow>
		</div>
	);
}

export default App;

