lc1 = 0.1;
lc2 = 0.25;

xl = -2;
xr = +2;
yl = -1;
yr = +1;

A = newp; Point(A) = {xl, yl, 0, lc1};
B = newp; Point(B) = {xr, yl, 0, lc1};
C = newp; Point(C) = {xr, yr, 0, lc1};
D = newp; Point(D) = {xl, yr, 0, lc1};

AB = newl; Line(AB) = {A, B};
BC = newl; Line(BC) = {B, C};
CD = newl; Line(CD) = {C, D};
DA = newl; Line(DA) = {D, A};
outer = newll; Curve Loop(outer) = {AB, BC, CD, DA};

Include "holes.geo";

model = news;
Plane Surface(model) = {outer, circle_11, circle_12, circle_13, circle_14, circle_15, circle_21, circle_22, circle_23, circle_24, circle_25, circle_31, circle_32, circle_33, circle_34, circle_35, circle_41, circle_42, circle_43, circle_44, circle_45, circle_51, circle_52, circle_53, circle_54, circle_55, circle_61, circle_62, circle_63, circle_64, circle_65, circle_71, circle_72, circle_73, circle_74, circle_75, circle_81, circle_82, circle_83, circle_84, circle_85, circle_91, circle_92, circle_93, circle_94, circle_95, circle_101, circle_102, circle_103, circle_104, circle_105, circle_111, circle_112, circle_113, circle_114, circle_115, circle_121, circle_122, circle_123, circle_124, circle_125, circle_131, circle_132, circle_133, circle_134, circle_135, circle_141, circle_142, circle_143, circle_144, circle_145, circle_151, circle_152, circle_153, circle_154, circle_155, circle_161, circle_162, circle_163, circle_164, circle_165, circle_171, circle_172, circle_173, circle_174, circle_175, circle_181, circle_182, circle_183, circle_184, circle_185, circle_191, circle_192, circle_193, circle_194, circle_195, circle_201, circle_202, circle_203, circle_204, circle_205, circle_211, circle_212, circle_213, circle_214, circle_215, circle_221, circle_222, circle_223, circle_224, circle_225, circle_231, circle_232, circle_233, circle_234, circle_235, circle_241, circle_242, circle_243, circle_244, circle_245};

Recombine Surface{model};
