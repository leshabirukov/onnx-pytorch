# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v7.Multinomial")
def Multinomial(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Multinomial"]
  omm.op_counter["Multinomial"] += 1
  node = onnx.helper.make_node("Multinomial",
                               _inputs, [f"_t_Multinomial_{idx}"],
                               name=f"Multinomial_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Asin")
def Asin(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Asin"]
  omm.op_counter["Asin"] += 1
  node = onnx.helper.make_node("Asin",
                               _inputs, [f"_t_Asin_{idx}"],
                               name=f"Asin_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Xor")
def Xor(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Xor"]
  omm.op_counter["Xor"] += 1
  node = onnx.helper.make_node("Xor",
                               _inputs, [f"_t_Xor_{idx}"],
                               name=f"Xor_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Upsample")
def Upsample(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Upsample"]
  omm.op_counter["Upsample"] += 1
  node = onnx.helper.make_node("Upsample",
                               _inputs, [f"_t_Upsample_{idx}"],
                               name=f"Upsample_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.And")
def And(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["And"]
  omm.op_counter["And"] += 1
  node = onnx.helper.make_node("And",
                               _inputs, [f"_t_And_{idx}"],
                               name=f"And_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Sub")
def Sub(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sub"]
  omm.op_counter["Sub"] += 1
  node = onnx.helper.make_node("Sub",
                               _inputs, [f"_t_Sub_{idx}"],
                               name=f"Sub_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Cos")
def Cos(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Cos"]
  omm.op_counter["Cos"] += 1
  node = onnx.helper.make_node("Cos",
                               _inputs, [f"_t_Cos_{idx}"],
                               name=f"Cos_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Mul")
def Mul(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Mul"]
  omm.op_counter["Mul"] += 1
  node = onnx.helper.make_node("Mul",
                               _inputs, [f"_t_Mul_{idx}"],
                               name=f"Mul_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Sin")
def Sin(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sin"]
  omm.op_counter["Sin"] += 1
  node = onnx.helper.make_node("Sin",
                               _inputs, [f"_t_Sin_{idx}"],
                               name=f"Sin_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.RNN")
def RNN(X, W, R, B=None, sequence_lens=None, initial_h=None, **kwargs):
  _inputs = []
  for i in (X, W, R, B, sequence_lens, initial_h):
    _add_input(i, _inputs)

  idx = omm.op_counter["RNN"]
  omm.op_counter["RNN"] += 1
  node = onnx.helper.make_node("RNN",
                               _inputs, [f"_t_RNN_{idx}"],
                               name=f"RNN_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Greater")
def Greater(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Greater"]
  omm.op_counter["Greater"] += 1
  node = onnx.helper.make_node("Greater",
                               _inputs, [f"_t_Greater_{idx}"],
                               name=f"Greater_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Or")
def Or(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Or"]
  omm.op_counter["Or"] += 1
  node = onnx.helper.make_node("Or",
                               _inputs, [f"_t_Or_{idx}"],
                               name=f"Or_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.BatchNormalization")
def BatchNormalization(X, scale, B, mean, var, **kwargs):
  _inputs = []
  for i in (X, scale, B, mean, var):
    _add_input(i, _inputs)

  idx = omm.op_counter["BatchNormalization"]
  omm.op_counter["BatchNormalization"] += 1
  node = onnx.helper.make_node("BatchNormalization",
                               _inputs, [f"_t_BatchNormalization_{idx}"],
                               name=f"BatchNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.LSTM")
def LSTM(X, W, R, B=None, sequence_lens=None, initial_h=None, initial_c=None, P=None, **kwargs):
  _inputs = []
  for i in (X, W, R, B, sequence_lens, initial_h, initial_c, P):
    _add_input(i, _inputs)

  idx = omm.op_counter["LSTM"]
  omm.op_counter["LSTM"] += 1
  node = onnx.helper.make_node("LSTM",
                               _inputs, [f"_t_LSTM_{idx}"],
                               name=f"LSTM_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Acos")
def Acos(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Acos"]
  omm.op_counter["Acos"] += 1
  node = onnx.helper.make_node("Acos",
                               _inputs, [f"_t_Acos_{idx}"],
                               name=f"Acos_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.PRelu")
def PRelu(X, slope, **kwargs):
  _inputs = []
  for i in (X, slope):
    _add_input(i, _inputs)

  idx = omm.op_counter["PRelu"]
  omm.op_counter["PRelu"] += 1
  node = onnx.helper.make_node("PRelu",
                               _inputs, [f"_t_PRelu_{idx}"],
                               name=f"PRelu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.GRU")
def GRU(X, W, R, B=None, sequence_lens=None, initial_h=None, **kwargs):
  _inputs = []
  for i in (X, W, R, B, sequence_lens, initial_h):
    _add_input(i, _inputs)

  idx = omm.op_counter["GRU"]
  omm.op_counter["GRU"] += 1
  node = onnx.helper.make_node("GRU",
                               _inputs, [f"_t_GRU_{idx}"],
                               name=f"GRU_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Tan")
def Tan(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Tan"]
  omm.op_counter["Tan"] += 1
  node = onnx.helper.make_node("Tan",
                               _inputs, [f"_t_Tan_{idx}"],
                               name=f"Tan_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Add")
def Add(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Add"]
  omm.op_counter["Add"] += 1
  node = onnx.helper.make_node("Add",
                               _inputs, [f"_t_Add_{idx}"],
                               name=f"Add_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Equal")
def Equal(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Equal"]
  omm.op_counter["Equal"] += 1
  node = onnx.helper.make_node("Equal",
                               _inputs, [f"_t_Equal_{idx}"],
                               name=f"Equal_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Pow")
def Pow(X, Y, **kwargs):
  _inputs = []
  for i in (X, Y):
    _add_input(i, _inputs)

  idx = omm.op_counter["Pow"]
  omm.op_counter["Pow"] += 1
  node = onnx.helper.make_node("Pow",
                               _inputs, [f"_t_Pow_{idx}"],
                               name=f"Pow_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Div")
def Div(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Div"]
  omm.op_counter["Div"] += 1
  node = onnx.helper.make_node("Div",
                               _inputs, [f"_t_Div_{idx}"],
                               name=f"Div_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Less")
def Less(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Less"]
  omm.op_counter["Less"] += 1
  node = onnx.helper.make_node("Less",
                               _inputs, [f"_t_Less_{idx}"],
                               name=f"Less_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Dropout")
def Dropout(data, **kwargs):
  _inputs = []
  for i in (data, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Dropout"]
  omm.op_counter["Dropout"] += 1
  node = onnx.helper.make_node("Dropout",
                               _inputs, [f"_t_Dropout_{idx}"],
                               name=f"Dropout_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Atan")
def Atan(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Atan"]
  omm.op_counter["Atan"] += 1
  node = onnx.helper.make_node("Atan",
                               _inputs, [f"_t_Atan_{idx}"],
                               name=f"Atan_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.AveragePool")
def AveragePool(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["AveragePool"]
  omm.op_counter["AveragePool"] += 1
  node = onnx.helper.make_node("AveragePool",
                               _inputs, [f"_t_AveragePool_{idx}"],
                               name=f"AveragePool_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v7.Gemm")
def Gemm(A, B, C, **kwargs):
  _inputs = []
  for i in (A, B, C):
    _add_input(i, _inputs)

  idx = omm.op_counter["Gemm"]
  omm.op_counter["Gemm"] += 1
  node = onnx.helper.make_node("Gemm",
                               _inputs, [f"_t_Gemm_{idx}"],
                               name=f"Gemm_{idx}",
                               **kwargs)
  onnx.checker.check_node(node)
  omm.model.graph.node.append(node)
  return node
