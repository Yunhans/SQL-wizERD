import React from 'react';
import ReactFlow, { Handle, Position } from 'reactflow';

const TableNode = ({ data }) => {
    return (
        <>
            <div className="mytable card" draggable="true" style={{ width: '300px' }}>
                <div className="myheader card-header d-flex px-2" draggable="true">
                    <span className="flex-grow-1 text-center">{data.label}</span>
                    <button type="button" className="btn btn-sm border-0 p-0" onClick={() => alert('edit table test')}>
                        <i className="bi bi-three-dots-vertical"></i>
                    </button>
                </div>
                <ul className="list-group list-group-flush my-1">
                    {data.attribute.map((attribute, index) => (
                        <li key={index} className="list-group-item border-0 py-1">
                            <div className="my-0 w-100 d-flex justify-content-between">
                                <span className="text-secondary">{attribute.name} {attribute.isKey && <i className="bi bi-key-fill text-warning"></i>}</span>
                                <span className="text-body-tertiary">{attribute.type}</span>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
            <Handle type="target" position={Position.Left} id="a" />
            <Handle type="source" position={Position.Right} id="b" />

        </>
    );
};

export default TableNode;