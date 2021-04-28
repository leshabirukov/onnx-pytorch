# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v5.Reshape")
def Reshape(data, shape, **kwargs):
  _inputs = []
  for i in (data, shape):
    _add_input(i, _inputs)

  idx = omm.op_counter["Reshape"]
  omm.op_counter["Reshape"] += 1
  node = onnx.helper.make_node("Reshape",
                               _inputs, [f"_t_Reshape_{idx}"],
                               name=f"Reshape_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node
