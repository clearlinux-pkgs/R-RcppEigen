#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppEigen
Version  : 0.3.2.9.0
Release  : 34
URL      : http://cran.r-project.org/src/contrib/RcppEigen_0.3.2.9.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/RcppEigen_0.3.2.9.0.tar.gz
Summary  : 'Rcpp' Integration for the 'Eigen' Templated Linear Algebra
Group    : Development/Tools
License  : GPL-2.0+ MPL-2.0
Requires: R-RcppEigen-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers
BuildRequires : eigen-dev

%description
## RcppEigen
[![Build Status](https://travis-ci.org/RcppCore/RcppEigen.svg)](https://travis-ci.org/RcppCore/RcppEigen) [![License](http://img.shields.io/badge/license-GPL%20%28%3E=%202%29-brightgreen.svg?style=flat)](http://www.gnu.org/licenses/gpl-2.0.html) [![License](http://img.shields.io/badge/license-MPL2-brightgreen.svg?style=flat)](http://www.mozilla.org/MPL/2.0/) [![CRAN](http://www.r-pkg.org/badges/version/RcppEigen)](http://cran.r-project.org/package=RcppEigen) [![Downloads](http://cranlogs.r-pkg.org/badges/RcppEigen?color=brightgreen)](http://www.r-pkg.org/pkg/RcppEigen)

%package lib
Summary: lib components for the R-RcppEigen package.
Group: Libraries

%description lib
lib components for the R-RcppEigen package.


%prep
%setup -q -c -n RcppEigen

%build
export LANG=C

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library RcppEigen
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RcppEigen


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppEigen/CITATION
/usr/lib64/R/library/RcppEigen/COPYRIGHTS
/usr/lib64/R/library/RcppEigen/DESCRIPTION
/usr/lib64/R/library/RcppEigen/INDEX
/usr/lib64/R/library/RcppEigen/LICENSE
/usr/lib64/R/library/RcppEigen/Meta/Rd.rds
/usr/lib64/R/library/RcppEigen/Meta/hsearch.rds
/usr/lib64/R/library/RcppEigen/Meta/links.rds
/usr/lib64/R/library/RcppEigen/Meta/nsInfo.rds
/usr/lib64/R/library/RcppEigen/Meta/package.rds
/usr/lib64/R/library/RcppEigen/Meta/vignette.rds
/usr/lib64/R/library/RcppEigen/NAMESPACE
/usr/lib64/R/library/RcppEigen/NEWS.Rd
/usr/lib64/R/library/RcppEigen/R/RcppEigen
/usr/lib64/R/library/RcppEigen/R/RcppEigen.rdb
/usr/lib64/R/library/RcppEigen/R/RcppEigen.rdx
/usr/lib64/R/library/RcppEigen/doc/RcppEigen-Introduction.R
/usr/lib64/R/library/RcppEigen/doc/RcppEigen-Introduction.Rnw
/usr/lib64/R/library/RcppEigen/doc/RcppEigen-Introduction.pdf
/usr/lib64/R/library/RcppEigen/doc/code.R
/usr/lib64/R/library/RcppEigen/doc/index.html
/usr/lib64/R/library/RcppEigen/doc/unitTests/RcppEigen-unitTests.R
/usr/lib64/R/library/RcppEigen/doc/unitTests/RcppEigen-unitTests.Rnw
/usr/lib64/R/library/RcppEigen/examples/lmBenchmark.R
/usr/lib64/R/library/RcppEigen/help/AnIndex
/usr/lib64/R/library/RcppEigen/help/RcppEigen.rdb
/usr/lib64/R/library/RcppEigen/help/RcppEigen.rdx
/usr/lib64/R/library/RcppEigen/help/aliases.rds
/usr/lib64/R/library/RcppEigen/help/paths.rds
/usr/lib64/R/library/RcppEigen/html/00Index.html
/usr/lib64/R/library/RcppEigen/html/R.css
/usr/lib64/R/library/RcppEigen/include/Eigen/Array
/usr/lib64/R/library/RcppEigen/include/Eigen/Cholesky
/usr/lib64/R/library/RcppEigen/include/Eigen/CholmodSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/Core
/usr/lib64/R/library/RcppEigen/include/Eigen/Dense
/usr/lib64/R/library/RcppEigen/include/Eigen/Eigen
/usr/lib64/R/library/RcppEigen/include/Eigen/Eigen2Support
/usr/lib64/R/library/RcppEigen/include/Eigen/Eigenvalues
/usr/lib64/R/library/RcppEigen/include/Eigen/Geometry
/usr/lib64/R/library/RcppEigen/include/Eigen/Householder
/usr/lib64/R/library/RcppEigen/include/Eigen/IterativeLinearSolvers
/usr/lib64/R/library/RcppEigen/include/Eigen/Jacobi
/usr/lib64/R/library/RcppEigen/include/Eigen/LU
/usr/lib64/R/library/RcppEigen/include/Eigen/LeastSquares
/usr/lib64/R/library/RcppEigen/include/Eigen/MetisSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/OrderingMethods
/usr/lib64/R/library/RcppEigen/include/Eigen/PaStiXSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/PardisoSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/QR
/usr/lib64/R/library/RcppEigen/include/Eigen/QtAlignedMalloc
/usr/lib64/R/library/RcppEigen/include/Eigen/SPQRSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/SVD
/usr/lib64/R/library/RcppEigen/include/Eigen/Sparse
/usr/lib64/R/library/RcppEigen/include/Eigen/SparseCholesky
/usr/lib64/R/library/RcppEigen/include/Eigen/SparseCore
/usr/lib64/R/library/RcppEigen/include/Eigen/SparseLU
/usr/lib64/R/library/RcppEigen/include/Eigen/SparseQR
/usr/lib64/R/library/RcppEigen/include/Eigen/StdDeque
/usr/lib64/R/library/RcppEigen/include/Eigen/StdList
/usr/lib64/R/library/RcppEigen/include/Eigen/StdVector
/usr/lib64/R/library/RcppEigen/include/Eigen/SuperLUSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/UmfPackSupport
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Cholesky/LDLT.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Cholesky/LLT.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Cholesky/LLT_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/CholmodSupport/CholmodSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Array.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/ArrayBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/ArrayWrapper.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Assign.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Assign_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/BandMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Block.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/BooleanRedux.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CommaInitializer.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CoreIterators.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CwiseBinaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CwiseNullaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CwiseUnaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/CwiseUnaryView.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/DenseBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/DenseCoeffsBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/DenseStorage.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Diagonal.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/DiagonalMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/DiagonalProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Dot.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/EigenBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Flagged.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/ForceAlignedAccess.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Functors.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Fuzzy.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/GeneralProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/GenericPacketMath.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/GlobalFunctions.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/IO.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Map.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/MapBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/MathFunctions.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Matrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/MatrixBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/NestByValue.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/NoAlias.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/NumTraits.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/PermutationMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/PlainObjectBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/ProductBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Random.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Redux.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Ref.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Replicate.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/ReturnByValue.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Reverse.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Select.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/SelfAdjointView.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/SelfCwiseBinaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/SolveTriangular.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/StableNorm.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Stride.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Swap.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Transpose.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Transpositions.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/TriangularMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/VectorBlock.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/VectorwiseOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/Visitor.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/AltiVec/Complex.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/AltiVec/PacketMath.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/Default/Settings.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/NEON/Complex.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/NEON/PacketMath.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/SSE/Complex.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/SSE/MathFunctions.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/arch/SSE/PacketMath.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/CoeffBasedProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralBlockPanelKernel.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixMatrixTriangular.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixMatrixTriangular_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixMatrix_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/GeneralMatrixVector_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/Parallelizer.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointMatrixMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointMatrixMatrix_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointMatrixVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointMatrixVector_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/SelfadjointRank2Update.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularMatrixMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularMatrixMatrix_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularMatrixVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularMatrixVector_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularSolverMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularSolverMatrix_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/products/TriangularSolverVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/BlasUtil.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/Constants.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/DisableStupidWarnings.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/ForwardDeclarations.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/MKL_support.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/Macros.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/Memory.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/Meta.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/NonMPL2.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/ReenableStupidWarnings.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/StaticAssert.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Core/util/XprHelper.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Block.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Cwise.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/CwiseOperators.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/AlignedBox.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/All.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/AngleAxis.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Hyperplane.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/ParametrizedLine.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Quaternion.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Rotation2D.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/RotationBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Scaling.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Transform.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Geometry/Translation.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/LU.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Lazy.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/LeastSquares.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Macros.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/MathFunctions.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Memory.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Meta.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/Minor.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/QR.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/SVD.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/TriangularSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigen2Support/VectorBlock.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/ComplexEigenSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/ComplexSchur.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/ComplexSchur_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/EigenSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/GeneralizedEigenSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/GeneralizedSelfAdjointEigenSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/HessenbergDecomposition.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/MatrixBaseEigenvalues.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/RealQZ.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/RealSchur.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/RealSchur_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/SelfAdjointEigenSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/SelfAdjointEigenSolver_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Eigenvalues/Tridiagonalization.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/AlignedBox.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/AngleAxis.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/EulerAngles.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Homogeneous.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Hyperplane.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/OrthoMethods.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/ParametrizedLine.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Quaternion.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Rotation2D.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/RotationBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Scaling.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Transform.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Translation.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/Umeyama.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Geometry/arch/Geometry_SSE.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Householder/BlockHouseholder.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Householder/Householder.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Householder/HouseholderSequence.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/IterativeLinearSolvers/BasicPreconditioners.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/IterativeLinearSolvers/BiCGSTAB.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/IterativeLinearSolvers/ConjugateGradient.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/IterativeLinearSolvers/IncompleteLUT.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/IterativeLinearSolvers/IterativeSolverBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/Jacobi/Jacobi.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/Determinant.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/FullPivLU.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/Inverse.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/PartialPivLU.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/PartialPivLU_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/LU/arch/Inverse_SSE.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/MetisSupport/MetisSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/OrderingMethods/Amd.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/OrderingMethods/Eigen_Colamd.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/OrderingMethods/Ordering.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/PaStiXSupport/PaStiXSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/PardisoSupport/PardisoSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/QR/ColPivHouseholderQR.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/QR/ColPivHouseholderQR_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/QR/FullPivHouseholderQR.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/QR/HouseholderQR.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/QR/HouseholderQR_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SPQRSupport/SuiteSparseQRSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SVD/JacobiSVD.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SVD/JacobiSVD_MKL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SVD/UpperBidiagonalization.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCholesky/SimplicialCholesky.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCholesky/SimplicialCholesky_impl.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/AmbiVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/CompressedStorage.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/ConservativeSparseSparseProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/MappedSparseMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseBlock.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseColEtree.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseCwiseBinaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseCwiseUnaryOp.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseDenseProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseDiagonalProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseDot.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseFuzzy.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseMatrixBase.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparsePermutation.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseProduct.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseRedux.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseSelfAdjointView.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseSparseProductWithPruning.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseTranspose.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseTriangularView.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseUtil.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/SparseView.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseCore/TriangularSolver.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLUImpl.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_Memory.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_Structs.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_SupernodalMatrix.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_Utils.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_column_bmod.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_column_dfs.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_copy_to_ucol.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_gemm_kernel.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_heap_relax_snode.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_kernel_bmod.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_panel_bmod.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_panel_dfs.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_pivotL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_pruneL.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseLU/SparseLU_relax_snode.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SparseQR/SparseQR.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/StlSupport/StdDeque.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/StlSupport/StdList.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/StlSupport/StdVector.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/StlSupport/details.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/SuperLUSupport/SuperLUSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/UmfPackSupport/UmfPackSupport.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/misc/Image.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/misc/Kernel.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/misc/Solve.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/misc/SparseSolve.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/misc/blas.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/ArrayCwiseBinaryOps.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/ArrayCwiseUnaryOps.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/BlockMethods.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/CommonCwiseBinaryOps.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/CommonCwiseUnaryOps.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/MatrixCwiseBinaryOps.h
/usr/lib64/R/library/RcppEigen/include/Eigen/src/plugins/MatrixCwiseUnaryOps.h
/usr/lib64/R/library/RcppEigen/include/RcppEigen.h
/usr/lib64/R/library/RcppEigen/include/RcppEigenCholmod.h
/usr/lib64/R/library/RcppEigen/include/RcppEigenForward.h
/usr/lib64/R/library/RcppEigen/include/RcppEigenStubs.h
/usr/lib64/R/library/RcppEigen/include/RcppEigenWrap.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/AdolcForward
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/AlignedVector3
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/ArpackSupport
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/AutoDiff
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/BVH
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/FFT
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/IterativeSolvers
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/KroneckerProduct
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/LevenbergMarquardt
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/MPRealSupport
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/MatrixFunctions
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/MoreVectorization
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/NonLinearOptimization
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/NumericalDiff
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/OpenGLSupport
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/Polynomials
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/SVD
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/Skyline
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/SparseExtra
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/Splines
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/AutoDiff/AutoDiffJacobian.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/AutoDiff/AutoDiffScalar.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/AutoDiff/AutoDiffVector.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/BVH/BVAlgorithms.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/BVH/KdBVH.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Eigenvalues/ArpackSelfAdjointEigenSolver.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/FFT/ei_fftw_impl.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/FFT/ei_kissfft_impl.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/ConstrainedConjGrad.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/DGMRES.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/GMRES.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/IncompleteCholesky.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/IncompleteLU.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/IterationController.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/MINRES.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/IterativeSolvers/Scaling.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/KroneckerProduct/KroneckerTensorProduct.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/CopyrightMINPACK.txt
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/LMcovar.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/LMonestep.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/LMpar.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/LMqrsolv.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/LevenbergMarquardt/LevenbergMarquardt.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixFunction.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixFunctionAtomic.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixLogarithm.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixPower.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/MatrixSquareRoot.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MatrixFunctions/StemFunction.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/MoreVectorization/MathFunctions.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/HybridNonLinearSolver.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/LevenbergMarquardt.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/chkder.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/covar.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/dogleg.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/fdjac1.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/lmpar.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/qrsolv.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/r1mpyq.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/r1updt.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NonLinearOptimization/rwupdt.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/NumericalDiff/NumericalDiff.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Polynomials/Companion.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Polynomials/PolynomialSolver.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Polynomials/PolynomialUtils.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SVD/BDCSVD.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SVD/JacobiSVD.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SVD/SVDBase.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SVD/TODOBdcsvd.txt
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SVD/doneInBDCSVD.txt
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineInplaceLU.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineMatrix.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineMatrixBase.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineProduct.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineStorage.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Skyline/SkylineUtil.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SparseExtra/BlockOfDynamicSparseMatrix.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SparseExtra/DynamicSparseMatrix.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SparseExtra/MarketIO.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SparseExtra/MatrixMarketIterator.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/SparseExtra/RandomSetter.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Splines/Spline.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Splines/SplineFitting.h
/usr/lib64/R/library/RcppEigen/include/unsupported/Eigen/src/Splines/SplineFwd.h
/usr/lib64/R/library/RcppEigen/libs/symbols.rds
/usr/lib64/R/library/RcppEigen/skeleton/Makevars
/usr/lib64/R/library/RcppEigen/skeleton/Makevars.win
/usr/lib64/R/library/RcppEigen/skeleton/rcppeigen_hello_world.Rd
/usr/lib64/R/library/RcppEigen/skeleton/rcppeigen_hello_world.cpp
/usr/lib64/R/library/RcppEigen/unitTests/runTests.R
/usr/lib64/R/library/RcppEigen/unitTests/runit.RcppEigen.R
/usr/lib64/R/library/RcppEigen/unitTests/runit.fastLm.R
/usr/lib64/R/library/RcppEigen/unitTests/runit.sparse.R
/usr/lib64/R/library/RcppEigen/unitTests/runit.transform.R
/usr/lib64/R/library/RcppEigen/unitTests/runit.wrap.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppEigen/libs/RcppEigen.so
/usr/lib64/R/library/RcppEigen/unitTests/runit.solutions.R
