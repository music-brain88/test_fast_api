// lib.rs
use pyo3::prelude::*;

#[pyfunction]
fn sum_as_string(a: i64, b: i64) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pymodule]
fn rust_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
