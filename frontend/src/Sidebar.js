import React, { useEffect, useRef } from 'react';
import { useStore } from '@xyflow/react';

const transformSelector = (state) => state.transform;

export default ({ nodes, setNodes }) => {
  const transform = useStore(transformSelector);

  const nodesRef = useRef(nodes);

  // Update the ref whenever nodes change
  useEffect(() => {
    nodesRef.current = nodes;
  }, [nodes]);

  // Expose nodesRef outside of React, e.g., to window object
  window.nodesRef = nodesRef;
  window.transform = transform;

  return (
    <aside>
      <div className="title">Zoom & pan transform</div>
      <div className="transform">
        [{transform[0].toFixed(2)}, {transform[1].toFixed(2)},{' '}
        {transform[2].toFixed(2)}]
      </div>
      <div className="title">Nodes</div>
      {nodes.map((node) => (
        <div key={node.id}>
            id:{node.id},
            x:{node.position.x.toFixed(2)},
            y:{node.position.y.toFixed(2)}
        </div>
      ))}
    </aside>
  );
};
