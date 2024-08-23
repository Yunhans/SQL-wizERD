import React from 'react';
import { Handle, Position } from '@xyflow/react';

const TableNode = ({ data }) => {
    return (
        <>
            <div className="mytable card" draggable="true" style={{ minWidth: '250px' }}>
                <div className="myheader card-header d-flex px-2" draggable="true">
                    <span className="flex-grow-1 text-center">{data.label}</span>
                    <button type="button" className="btn btn-sm border-0 p-0" onClick={ () => { const message = JSON.stringify({ action: 'edit info', table_id: data.id }); window.parent.postMessage(message, 'http://127.0.0.1:8000/whiteboard/'); } } data-bs-toggle="modal" data-bs-target="#editTableModal">
                        <i className="bi bi-three-dots-vertical"></i>
                    </button>
                </div>
                <ul className="list-group list-group-flush my-1">
                    { data.attribute.map((attribute, index) => (
                        <li key={index} className="list-group-item border-0 py-1">
                            <div className="my-0 w-100 d-flex justify-content-between">
                                <span className="text-secondary">{attribute.name} {attribute.isKey && <i className="bi bi-key-fill text-warning"></i>}</span>
                                <span className="text-body-tertiary ms-4">{attribute.type}</span>
                            </div>
                            {/* <Handle type="source" position={Position.Right} id={attribute.name + "-a"}/>
                            <Handle type="source" position={Position.Left} id={attribute.name + "-b"}/> */}
                        </li>
                    ))}
                </ul>
            </div>
            <Handle type="source" position={Position.Right} id="a" />
            <Handle type="source" position={Position.Left} id="b" />
            <Handle type="source" position={Position.Top} id="c" />
            <Handle type="source" position={Position.Bottom} id="d" />
        </>
    );
};

export default TableNode;