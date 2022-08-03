# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v15.CastLike")
def CastLike(input, target_type, **kwargs):
  _inputs = []
  for i in (input, target_type):
    _add_input(i, _inputs)

  idx = omm.op_counter["CastLike"]
  omm.op_counter["CastLike"] += 1
  node = onnx.helper.make_node("CastLike",
                               _inputs, [f'_t_CastLike_{idx}_output'],
                               name=f"CastLike_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.OptionalGetElement")
def OptionalGetElement(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["OptionalGetElement"]
  omm.op_counter["OptionalGetElement"] += 1
  node = onnx.helper.make_node("OptionalGetElement",
                               _inputs, [f'_t_OptionalGetElement_{idx}_output'],
                               name=f"OptionalGetElement_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.Optional")
def Optional(input=None, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Optional"]
  omm.op_counter["Optional"] += 1
  node = onnx.helper.make_node("Optional",
                               _inputs, [f'_t_Optional_{idx}_output'],
                               name=f"Optional_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.Shape")
def Shape(data, **kwargs):
  _inputs = []
  for i in (data, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Shape"]
  omm.op_counter["Shape"] += 1
  node = onnx.helper.make_node("Shape",
                               _inputs, [f'_t_Shape_{idx}_shape'],
                               name=f"Shape_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.OptionalHasElement")
def OptionalHasElement(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["OptionalHasElement"]
  omm.op_counter["OptionalHasElement"] += 1
  node = onnx.helper.make_node("OptionalHasElement",
                               _inputs, [f'_t_OptionalHasElement_{idx}_output'],
                               name=f"OptionalHasElement_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.Bernoulli")
def Bernoulli(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Bernoulli"]
  omm.op_counter["Bernoulli"] += 1
  node = onnx.helper.make_node("Bernoulli",
                               _inputs, [f'_t_Bernoulli_{idx}_output'],
                               name=f"Bernoulli_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.BatchNormalization")
def BatchNormalization(X, scale, B, input_mean, input_var, **kwargs):
  _inputs = []
  for i in (X, scale, B, input_mean, input_var):
    _add_input(i, _inputs)

  idx = omm.op_counter["BatchNormalization"]
  omm.op_counter["BatchNormalization"] += 1
  node = onnx.helper.make_node("BatchNormalization",
                               _inputs, [f'_t_BatchNormalization_{idx}_Y'],
                               name=f"BatchNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v15.Pow")
def Pow(X, Y, **kwargs):
  _inputs = []
  for i in (X, Y):
    _add_input(i, _inputs)

  idx = omm.op_counter["Pow"]
  omm.op_counter["Pow"] += 1
  node = onnx.helper.make_node("Pow",
                               _inputs, [f'_t_Pow_{idx}_Z'],
                               name=f"Pow_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node
