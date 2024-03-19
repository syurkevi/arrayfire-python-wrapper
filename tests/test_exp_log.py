import random
import pytest

import arrayfire_wrapper.dtypes as dtype
import arrayfire_wrapper.lib as wrapper


dtype_map = {
    'int16': dtype.s16,
    'int32': dtype.s32,
    'int64': dtype.s64,
    'uint8': dtype.u8,
    'uint16': dtype.u16,
    'uint32': dtype.u32,
    'uint64': dtype.u64,
    'float16': dtype.f16,
    'float32': dtype.f32,
    # 'float64': dtype.f64,
    # 'complex64': dtype.c64,
    # 'complex32': dtype.c32,
    'bool': dtype.b8,
    's16': dtype.s16,
    's32': dtype.s32,
    's64': dtype.s64,
    'u8': dtype.u8,
    'u16': dtype.u16,
    'u32': dtype.u32,
    'u64': dtype.u64,
    'f16': dtype.f16,
    'f32': dtype.f32,
    # 'f64': dtype.f64,
    # 'c32': dtype.c32,
    # 'c64': dtype.c64,
    'b8': dtype.b8,
}
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_cbrt_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test cube root operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.cbrt(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_cbrt_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test cube root operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.cbrt(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_erf_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test gaussian error operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.erf(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_erf_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test gaussian error operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.erf(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_erfc_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test gaussian error complement operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.erfc(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_erfc_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test gaussian error complement operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.erfc(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_exp_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test exponent operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.exp(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_exp_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test exponent operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.exp(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_exp1_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test exponent - 1 operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.expm1(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_exp_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test exponent - 1 operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.expm1(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_exp_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test exponent operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.exp(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_exp_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test exponent operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.exp(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_fac_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test exponent operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.factorial(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_fac_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test exponent operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.factorial(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_lgamma_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test lgamma operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.lgamma(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_lgamma_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test lgamma operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.lgamma(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_log_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test log operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.log(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_log_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test log operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.log(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_log10_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test log10 operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.log10(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_log10_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test log10 operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.log10(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_log1p_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test natural logarithm of 1 + input operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.log1p(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_log1p_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test logarithm of 1 + input operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.log1p(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_log2_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test log2 operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.log2(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_log2_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test log2 operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.log2(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_pow_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test power operation across all supported data types."""
    lhs = wrapper.randu(shape, dtype_name)
    rhs = wrapper.randu(shape, dtype_name)
    result = wrapper.pow(lhs, rhs)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 

@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_pow_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test power operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.pow(wrapper.randu((10,), invdtypes), wrapper.randu((10, invdtypes)))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_root_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test root operation across all supported data types."""
    lhs = wrapper.randu(shape, dtype_name)
    rhs = wrapper.randu(shape, dtype_name)
    result = wrapper.root(lhs, rhs)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 

@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_root_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test root operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.root(wrapper.randu((10,), invdtypes), wrapper.randu((10, invdtypes)))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_pow2_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test 2 to power operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.pow2(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_pow2_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test 2 to power operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.pow2(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_rsqrt_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test reciprocal square root operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.rsqrt(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_rsqrt_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test reciprocal square root operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.rsqrt(wrapper.randu((10,), invdtypes))
@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_sqrt_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test  square root operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.sqrt(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_sqrt_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test square root operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.sqrt(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_tgamma_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test gamma operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.tgamma(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_tgamma_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test gamma operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.tgamma(wrapper.randu((10,), invdtypes))

@pytest.mark.parametrize(
    "shape",
    [
        (),
        (random.randint(1, 10), ),
        (random.randint(1, 10),),
        (random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
        (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)),
    ],
)
@pytest.mark.parametrize("dtype_name", dtype_map.values())
def test_sigmoid_shape_dtypes(shape:tuple, dtype_name: dtype.Dtype) -> None:
    """Test sigmoid operation across all supported data types."""
    values = wrapper.randu(shape, dtype_name)
    result = wrapper.sigmoid(values)
    assert wrapper.get_dims(result)[0:len(shape)] == shape, f"failed for shape: {shape}" 
@pytest.mark.parametrize(
    "invdtypes",
    [
        dtype.c64,
        dtype.f64,
    ],
)
def test_sigmoid_unsupported_dtypes(invdtypes: dtype.Dtype) -> None:
    """Test sigmoid operation for unsupported data types."""
    with pytest.raises(RuntimeError):
        wrapper.sigmoid(wrapper.randu((10,), invdtypes))
