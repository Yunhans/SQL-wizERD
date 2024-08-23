import { getBezierPath, useInternalNode } from '@xyflow/react';

import { getEdgeParams } from './utils.js';

function SimpleFloatingEdge({ id, source, target, markerStart, style }) {
  const sourceNode = useInternalNode(source);
  const targetNode = useInternalNode(target);

  const { sx, sy, tx, ty, sourcePos, targetPos } = getEdgeParams(
    sourceNode,
    targetNode,
  );

  const [edgePath] = getBezierPath({
    sourceX: sx,
    sourceY: sy,
    sourcePosition: sourcePos,
    targetPosition: targetPos,
    targetX: tx,
    targetY: ty,
  });

  return (
    <path
      id={id}
      className="react-flow__edge-path"
      d={edgePath}
      strokeWidth={5}
      markerStart={markerStart}
      style={style}
    />
  );
}

export default SimpleFloatingEdge;
