# CHANGELOG



## v3.6.2 (2024-03-08)

### Chore

* chore(SemanticRelease): decommission semantic-release js - move responsibility to python-semantic-release and manually publish ([`a4bec8c`](https://github.com/blockchain-certificates/cert-schema/commit/a4bec8c3d289efd84df82ebefa315806c1071497))

* chore(Tox): prevent failure due to accessing cert_schema files before installing deps ([`5091bf5`](https://github.com/blockchain-certificates/cert-schema/commit/5091bf5fca67ab1d7f218e94c83592328b40eced))

* chore(CI): align travis config to cert_issuer&#39;s ([`a9bd524`](https://github.com/blockchain-certificates/cert-schema/commit/a9bd52481b0230a3ce20f46c542fe9068f699469))

* chore(CI): try and force requests install ([`9fc78a5`](https://github.com/blockchain-certificates/cert-schema/commit/9fc78a5e1049dab06a66b3914881b3e8967bc148))

* chore(SemanticRelease): run PRs only against master ([`8dd7fbf`](https://github.com/blockchain-certificates/cert-schema/commit/8dd7fbf0922a1612764ad152e82713235b01451f))

* chore(SemanticRelease): configure python-semantic-release for &gt; v7 ([`6baac50`](https://github.com/blockchain-certificates/cert-schema/commit/6baac5082cd0a05d0f3b3bc00bf85ec3dfc665d2))

### Fix

* fix(DataIntegrityProof): correct name for data integrity proof property ([`c2cea4f`](https://github.com/blockchain-certificates/cert-schema/commit/c2cea4fd647b9f8a1aec17f704c2660112c5058c))

### Refactor

* refactor(JsonLdHelpers): use urllib rather than requests ([`5471e6c`](https://github.com/blockchain-certificates/cert-schema/commit/5471e6cb3d467bbaa53d3dbf0bc847d5e198cefb))

### Unknown

* Merge pull request #61 from blockchain-certificates/chore/fix-semantic-release

chore(SemanticRelease): decommission semantic-release js - move respo… ([`79b20ec`](https://github.com/blockchain-certificates/cert-schema/commit/79b20ecdd63dea1289abdf0dfd20456438777414))

* Merge pull request #60 from blockchain-certificates/chore/fix-semantic-release

chore(SemanticRelease): configure python-semantic-release for &gt; v7 ([`d62cc64`](https://github.com/blockchain-certificates/cert-schema/commit/d62cc6410e5c8ef2f86a760fb79e04ef0d7048ef))

* Merge pull request #59 from blockchain-certificates/feat/expose-data-integrity-proof-ctx

fix(DataIntegrityProof): correct name for data integrity proof property ([`6588c07`](https://github.com/blockchain-certificates/cert-schema/commit/6588c07b19f7337ae08755ac6da86bf280db21d2))


## v3.6.1 (2024-02-27)

### Chore

* chore(Deps): update pyld version ([`fd71457`](https://github.com/blockchain-certificates/cert-schema/commit/fd714578759dfc9509ebf67daccd0a494754b9c8))

### Fix

* fix(npm): fix path to credential v2 context ([`93f5fa7`](https://github.com/blockchain-certificates/cert-schema/commit/93f5fa796c918c934715751f2807b2e2c05b17ef))

### Unknown

* Merge pull request #58 from blockchain-certificates/feat/expose-data-integrity-proof-ctx

Feat/expose data integrity proof ctx ([`96273bc`](https://github.com/blockchain-certificates/cert-schema/commit/96273bc034b3b036744cbdef3fed28a1469d9737))


## v3.6.0 (2024-02-14)

### Feature

* feat(DataIntegrityProof): support data integrity proof ([`bcfd38c`](https://github.com/blockchain-certificates/cert-schema/commit/bcfd38c677558a8f108641972893b28706fd96b0))

### Unknown

* Merge pull request #57 from blockchain-certificates/feat/expose-data-integrity-proof-ctx

feat(DataIntegrityProof): support data integrity proof ([`2615b85`](https://github.com/blockchain-certificates/cert-schema/commit/2615b8537bc199d1efb11e8e72751870ad36974e))


## v3.5.1 (2024-01-30)

### Chore

* chore(CI): bump node ([`2db830d`](https://github.com/blockchain-certificates/cert-schema/commit/2db830d3ccc15d7f6c09df8eecbe12c2f126413a))

### Fix

* fix(VC-V2): expose vc V2 in document loader ([`9928854`](https://github.com/blockchain-certificates/cert-schema/commit/99288540b72bb8aeb1734a25f542f64b748c0d19))

### Unknown

* Merge pull request #56 from blockchain-certificates/fix/expose-vc-v2-in-context-urls

fix(VC-V2): expose vc V2 in document loader ([`b7d3636`](https://github.com/blockchain-certificates/cert-schema/commit/b7d3636d01d1a1dc0be0d43ebd4b44973d12a718))

* Merge pull request #55 from blockchain-certificates/feat/convert-to-esm

chore(CI): bump node ([`3125895`](https://github.com/blockchain-certificates/cert-schema/commit/3125895474a70bf790f63ed92c81d821a53b22c4))


## v3.5.0 (2024-01-29)

### Feature

* feat(VC-V2): provide verifiable credentials v2 ([`17332a2`](https://github.com/blockchain-certificates/cert-schema/commit/17332a2a94dae4a77a3b62749436f13cf438aa11))

* feat(Module): convert package to module ([`7da70a8`](https://github.com/blockchain-certificates/cert-schema/commit/7da70a87b10e6b9634e38de631a899231d5bcb06))

### Unknown

* Merge pull request #54 from blockchain-certificates/feat/convert-to-esm

Add VC V2 schema and convert to ESM ([`1a2993e`](https://github.com/blockchain-certificates/cert-schema/commit/1a2993e5f87ed8be14edd809fe2483c5e76d534f))


## v3.4.2 (2023-05-17)

### Chore

* chore(CI): bump to python 3.10 ([`3b865db`](https://github.com/blockchain-certificates/cert-schema/commit/3b865db83d913117be0fd4b2650edb0b7ea898fe))

### Fix

* fix(API): expose document loader function ([`df4422a`](https://github.com/blockchain-certificates/cert-schema/commit/df4422a8a17502f1dad30cf6739e9fccd7836e5a))

### Unknown

* Merge pull request #53 from blockchain-certificates/fix/expose-document-loader

Fix/expose document loader ([`cdda06f`](https://github.com/blockchain-certificates/cert-schema/commit/cdda06f290459bac471be41c2d12e1033ead4ce0))

* Merge branch &#39;master&#39; of https://github.com/blockchain-certificates/cert-schema ([`d1831ae`](https://github.com/blockchain-certificates/cert-schema/commit/d1831aeac0142f15872fe5798128c76b872d14c5))


## v3.4.1 (2023-03-30)

### Fix

* fix(Schemas): correct path to context ([`4375b57`](https://github.com/blockchain-certificates/cert-schema/commit/4375b5780a5b3f0ee4948038d52d982a431b1a3d))

* fix(Schemas): correct path to context ([`6102560`](https://github.com/blockchain-certificates/cert-schema/commit/610256079083c821f4715b2c621258104f246aee))

### Unknown

* Merge pull request #52 from blockchain-certificates/feat/status-list-2021

fix(Schemas): correct path to context ([`90cc814`](https://github.com/blockchain-certificates/cert-schema/commit/90cc81405608c8e832e6c9750a848fd5914535b1))


## v3.4.0 (2023-03-30)

### Feature

* feat(All): trigger new release ([`6bab8b4`](https://github.com/blockchain-certificates/cert-schema/commit/6bab8b424d8baac1a1ba5e2eefa083d6ebd0ace2))

### Unknown

* Merge pull request #51 from blockchain-certificates/feat/status-list-2021

feat(All): trigger new release ([`957714b`](https://github.com/blockchain-certificates/cert-schema/commit/957714b9845bd59cb33e0b7e1cfa107445a74140))


## v3.3.0 (2023-03-30)

### Chore

* chore(CI): debug ([`9507cd6`](https://github.com/blockchain-certificates/cert-schema/commit/9507cd64d8c0e5286fbf5e71112b57b7325a8d79))

* chore(semanticRelease): no dry run in js mode ([`4c12fb4`](https://github.com/blockchain-certificates/cert-schema/commit/4c12fb4eba4db1e73f361f73fe018f25659282a3))

* chore(SemanticRelease): cd back to root ([`77c27bc`](https://github.com/blockchain-certificates/cert-schema/commit/77c27bc2ba6a6eb6c32bbf6c78294aa49a7eb610))

* chore(SemanticRelease): delegate github tag to python script to avoid duplicate increment ([`3ac51ec`](https://github.com/blockchain-certificates/cert-schema/commit/3ac51ec670ebbb2fad8a412bc6d8bcf2c385b446))

* chore(SemanticRelease): split version file ([`188441e`](https://github.com/blockchain-certificates/cert-schema/commit/188441e2910a919e974b29bb4c86d05f2312d384))

* chore(CI): install requirements with tox ([`3fb8438`](https://github.com/blockchain-certificates/cert-schema/commit/3fb843829324b8871cc52eeb5f7f57111eb4a806))

* chore(CI): install requirements ([`f221a00`](https://github.com/blockchain-certificates/cert-schema/commit/f221a00bd3b89f1c3f55e559d955c087c087a161))

* chore(CI): configure semantic release in dry mode ([`878f0c9`](https://github.com/blockchain-certificates/cert-schema/commit/878f0c976b974658b422de3f000f911cdc237392))

### Documentation

* docs(Metadata): document metadata property ([`1bbbf87`](https://github.com/blockchain-certificates/cert-schema/commit/1bbbf872d0a8c163a181a0999e164cdb653314b3))

### Feature

* feat(StatusList2021): add StatusList2021 context ([`0ef1548`](https://github.com/blockchain-certificates/cert-schema/commit/0ef1548ca184cf4f525e91aca9d08a4f32eb2e9a))

### Unknown

* Merge pull request #50 from blockchain-certificates/feat/status-list-2021

chore(semanticRelease): no dry run in js mode ([`fdef509`](https://github.com/blockchain-certificates/cert-schema/commit/fdef509d4cceb409f9e9e9bcb64271606295c84e))

* Merge pull request #49 from blockchain-certificates/feat/status-list-2021

feat(StatusList2021): add StatusList2021 context ([`b7a8758`](https://github.com/blockchain-certificates/cert-schema/commit/b7a8758f22e9465a46a6621a4dc84974b8176662))

* Merge pull request #48 from blockchain-certificates/chore/semantic-release-python

chore(SemanticRelease): cd back to root ([`4ec7e79`](https://github.com/blockchain-certificates/cert-schema/commit/4ec7e792d4f12d2a58fc4da4b1536609cf470c65))

* Merge pull request #47 from blockchain-certificates/chore/semantic-release-python

chore(SemanticRelease): delegate github tag to python script to avoid duplicate increment ([`52e8489`](https://github.com/blockchain-certificates/cert-schema/commit/52e84899751a86e0c475fa562b8c29020741779d))

* Merge pull request #46 from blockchain-certificates/chore/semantic-release-python

chore(CI): configure semantic release in dry mode ([`39e44d1`](https://github.com/blockchain-certificates/cert-schema/commit/39e44d12d1246424dfafdaeb5a2992d79aaacfdf))

* Merge pull request #45 from blockchain-certificates/docs/metadata

docs(Metadata): document metadata property ([`1d1be91`](https://github.com/blockchain-certificates/cert-schema/commit/1d1be9122049cb2fdf1fecd947e91c1bbfbff86e))


## v3.2.1 (2022-06-20)

### Fix

* fix(MultiSign): reference contexts in js module ([`410e943`](https://github.com/blockchain-certificates/cert-schema/commit/410e94394bd05c4aebbdd1b8309a565fc8cc0041))

### Unknown

* Merge pull request #44 from blockchain-certificates/feat/multisign

fix(MultiSign): reference contexts in js module ([`5b2dc5a`](https://github.com/blockchain-certificates/cert-schema/commit/5b2dc5a491017418d971adfe169349838a065e35))


## v3.2.0 (2022-06-20)

### Feature

* feat(MultiSign): bump version ([`ab7958d`](https://github.com/blockchain-certificates/cert-schema/commit/ab7958d84d1b8267a4652c26da40e1d0560cfb99))

* feat(MultiSign): define suite contexts object ([`ce301a9`](https://github.com/blockchain-certificates/cert-schema/commit/ce301a93a83233a4ed11efb2803e695fcc61362b))

* feat(MultiSign): allow extending preloaded contexts before normalization ([`7110921`](https://github.com/blockchain-certificates/cert-schema/commit/71109210b2942276e0b04ff943cd403300f70ff0))

* feat(v3.1): introduce 3.1 concern ([`748ee8a`](https://github.com/blockchain-certificates/cert-schema/commit/748ee8af3b6c1abf82f80fbbd666b4a2a52ea765))

* feat(MultiSign): split MerkleProof2019 from Blockcerts context, define other required contexts ([`a9c2b85`](https://github.com/blockchain-certificates/cert-schema/commit/a9c2b8586a4c69b6731bd79e530c3920cddec148))

### Refactor

* refactor(Test): rename tests to better reflect test case ([`19b1ed4`](https://github.com/blockchain-certificates/cert-schema/commit/19b1ed4be9cf0f961085da7261816275baddcc8b))

### Test

* test(JSONLDNormalize): add proper test check ([`e14ae3b`](https://github.com/blockchain-certificates/cert-schema/commit/e14ae3bc7dd6ea606e9a9dbbe064ed0169ca42b9))

### Unknown

* Merge pull request #43 from blockchain-certificates/feat/multisign

Feat/multisign ([`3aba646`](https://github.com/blockchain-certificates/cert-schema/commit/3aba646f44f8ebe0a39de905694e88fcea1bdb68))


## v3.1.0 (2022-04-08)

### Chore

* chore(Version): bump version ([`1d10f7b`](https://github.com/blockchain-certificates/cert-schema/commit/1d10f7b9fa647af6234e2c7b4ef27f8f8d3b2a33))

* chore(CI): fix script path according to current working directory ([`26f5799`](https://github.com/blockchain-certificates/cert-schema/commit/26f57999e437576a769a34fcb1df44a02e7277eb))

* chore(CI): debug script issue ([`b8d2dcb`](https://github.com/blockchain-certificates/cert-schema/commit/b8d2dcbd448b6d92318223f73ef606d472ae37b8))

* chore(Release): fix typo ([`0001c63`](https://github.com/blockchain-certificates/cert-schema/commit/0001c63e08c76e4a769d559a9b6d583a6b20881d))

* chore(Publish): automatically publish to blockcerts.org ([`a09ce57`](https://github.com/blockchain-certificates/cert-schema/commit/a09ce577f593a7ee281b904bd1dc5b738081d4bf))

### Feature

* feat(ContextUrls): consume class where relevant ([`54599f6`](https://github.com/blockchain-certificates/cert-schema/commit/54599f6308fcb6072c277e7b4308746392eb83ec))

* feat(ContextUrls): add open badge and vc ([`8d91e6e`](https://github.com/blockchain-certificates/cert-schema/commit/8d91e6efc6526fcddc928ae00f15e422d1a9e059))

* feat(ContextUrls): add v2.1 and v3 getters ([`9955306`](https://github.com/blockchain-certificates/cert-schema/commit/9955306d90984d8132542515960e268ffb9965b6))

* feat(ContextUrls): provide getter class for context urls data ([`933b6f6`](https://github.com/blockchain-certificates/cert-schema/commit/933b6f693201639a45e4434a2683129d96c2ce03))

### Unknown

* Merge pull request #42 from blockchain-certificates/feat/context_url_getter

Feat/context url getter ([`8b28336`](https://github.com/blockchain-certificates/cert-schema/commit/8b28336df2330d9e6af691921d2ab9d4131ff14f))

* Merge pull request #41 from blockchain-certificates/chore/automated-updates-blockcerts.org

chore(CI): debug script issue ([`6e9c42e`](https://github.com/blockchain-certificates/cert-schema/commit/6e9c42e02949effbfd222a428573fafed3f6c974))

* Merge pull request #40 from blockchain-certificates/chore/automated-updates-blockcerts.org

chore(Publish): automatically publish to blockcerts.org ([`be31b0e`](https://github.com/blockchain-certificates/cert-schema/commit/be31b0e4c6e934d551b8c518d0ae648e056d906f))


## v3.0.7 (2022-04-05)

### Fix

* fix(Context): fix typo in export instruction ([`88cd797`](https://github.com/blockchain-certificates/cert-schema/commit/88cd7974e379e03682be569c2cd4f008fbe250ce))

### Unknown

* Merge pull request #39 from blockchain-certificates/fix/context-urls

fix(Context): fix typo in export instruction ([`58ffc14`](https://github.com/blockchain-certificates/cert-schema/commit/58ffc14587f9fbe695f2cd9440c4041ebab81fc4))


## v3.0.6 (2022-04-05)

### Chore

* chore(Version): align py version to npm ([`4b68fb4`](https://github.com/blockchain-certificates/cert-schema/commit/4b68fb44642143ea3ae39aa9980c78ad5fc05c74))

### Fix

* fix(Context): expose context urls to py package ([`24ad5c3`](https://github.com/blockchain-certificates/cert-schema/commit/24ad5c3b89ff53e957c0a6a368476007e11f09a8))

### Unknown

* Merge pull request #38 from blockchain-certificates/fix/context-urls

fix(Context): expose context urls to py package ([`7fd3406`](https://github.com/blockchain-certificates/cert-schema/commit/7fd34064c4a20585806edfddb5e8f15c0d80922a))

* Merge pull request #37 from blockchain-certificates/chore/npm-package

chore(Version): align py version to npm ([`11d7e4b`](https://github.com/blockchain-certificates/cert-schema/commit/11d7e4b75f23765ee1e63011eb82cfcc9881dbd6))


## v3.0.5 (2022-04-05)

### Chore

* chore(CI): update repository address ([`f20cdee`](https://github.com/blockchain-certificates/cert-schema/commit/f20cdee859dfa4aa2f91a60128d693890ce4b6f1))

* chore(CI): install and run node ([`c854d61`](https://github.com/blockchain-certificates/cert-schema/commit/c854d6160d2c8ed78a90dd0af1c70b6fc92d2fa3))

* chore(CI): fix node version ([`a8b9769`](https://github.com/blockchain-certificates/cert-schema/commit/a8b976928c90efcfbc9a6c5d6555e2252a8fe15f))

* chore(CI): manually install semantic-release ([`d18683b`](https://github.com/blockchain-certificates/cert-schema/commit/d18683ba516228d23166930b6902335e960d9937))

* chore(Version): bump py version ([`47ae086`](https://github.com/blockchain-certificates/cert-schema/commit/47ae08696140f8ad23fa7965d272aea6cbdc29c7))

* chore(CI): configure semantic release for NPM ([`240d1ef`](https://github.com/blockchain-certificates/cert-schema/commit/240d1efb3a50ad2dda2349e9f7812ccf885b34de))

### Fix

* fix(JsonLd): fix variables ([`6b25d35`](https://github.com/blockchain-certificates/cert-schema/commit/6b25d357e6a1d0826601dbd08094f2492cec0cab))

* fix(Context): fix typo ([`94e9b43`](https://github.com/blockchain-certificates/cert-schema/commit/94e9b43c0a46b596f834ef85dec46e5bdcbf38d2))

### Style

* style(All): remove trailing print ([`e175923`](https://github.com/blockchain-certificates/cert-schema/commit/e1759236b11ece67b9bbe42ea18ee57687ecb7ed))

### Unknown

* Merge pull request #36 from blockchain-certificates/chore/npm-package

Chore/npm package ([`ffd9f51`](https://github.com/blockchain-certificates/cert-schema/commit/ffd9f51bb343410d716e44413ba1d6bdf02cc672))


## v3.0.4 (2022-04-05)

### Chore

* chore(Release): update release steps ([`67a4e11`](https://github.com/blockchain-certificates/cert-schema/commit/67a4e1180dfa6fa70d7c8e2a48300576f70f6332))

* chore(Version): bump version ([`df5082f`](https://github.com/blockchain-certificates/cert-schema/commit/df5082f3cc4cf900fadb8e0eae4b60ccc84c278f))

* chore(CI): update python version ([`a5c89f4`](https://github.com/blockchain-certificates/cert-schema/commit/a5c89f484a66e40fb126888cc3b75be8dd4d3fc7))

* chore(NPM): prepare structure for npm package ([`183e1f0`](https://github.com/blockchain-certificates/cert-schema/commit/183e1f0d54b47360756bb21a59b24c5af24bdcce))

### Feature

* feat(NPM): create shared data between py and js to centralize source of truth ([`624dcde`](https://github.com/blockchain-certificates/cert-schema/commit/624dcde2d7c1f58a81755c2a2b4efe18639b1497))

* feat(v3): better support of hashing ([`7be37c8`](https://github.com/blockchain-certificates/cert-schema/commit/7be37c8709e070289e89a7c0cbeed57f4c82dcfd))

* feat(v3): fix v3 tests ([`6455276`](https://github.com/blockchain-certificates/cert-schema/commit/6455276fd17f41e17ece5beebdea24550a9a52a1))

* feat(v3): prepare code for v3 ([`173a052`](https://github.com/blockchain-certificates/cert-schema/commit/173a052fbc9cb9c4be3615ae7b10755349f496ed))

* feat(v3): remove hashed property as it does not support a proper use case ([`07839d3`](https://github.com/blockchain-certificates/cert-schema/commit/07839d34c3cbb5cc24fa1272d4c97c09620c8b96))

* feat(V3): define v3 properties and versionning ([`9863915`](https://github.com/blockchain-certificates/cert-schema/commit/9863915024f3f511f2b6cd17b635309204c68124))

* feat(v3b): bump version ([`4234e97`](https://github.com/blockchain-certificates/cert-schema/commit/4234e97b36a2a1ed86073ad69dcb539925ad1472))

* feat(v3b): define more keys for blockcerts model ([`24d125a`](https://github.com/blockchain-certificates/cert-schema/commit/24d125a9d1f4f54835acc40c7dfc7de1c63de19b))

* feat(v3b): prepare package for release ([`43e21d1`](https://github.com/blockchain-certificates/cert-schema/commit/43e21d1f5937b4081391a932bfb148b02bf68e66))

* feat(v3b): reference v3 beta addresses ([`1e7f11f`](https://github.com/blockchain-certificates/cert-schema/commit/1e7f11f982ffd70280f8d9d1506b585f9edd16d8))

* feat(v3b): list VC contexts ([`7fc11b2`](https://github.com/blockchain-certificates/cert-schema/commit/7fc11b2c27308135ab98a1c6ecd127fb7f65fa28))

* feat(V3Beta): normalize display property ([`c4e5f18`](https://github.com/blockchain-certificates/cert-schema/commit/c4e5f18f378d5470e9ccee590c62d9bb1fa023b8))

* feat(Metadata): define metadata object ([`05e5976`](https://github.com/blockchain-certificates/cert-schema/commit/05e59762baa3fc2591e6c976d2e00f27e34016cd))

* feat(3.0-beta): added attempt for metadata ([`b59b65e`](https://github.com/blockchain-certificates/cert-schema/commit/b59b65e81802ca244ab4be1f805b2df018afa69c))

### Fix

* fix(JsonLd): fix preloading URL for blockcert.org ([`af3cc64`](https://github.com/blockchain-certificates/cert-schema/commit/af3cc6404fd8a781bd51094fbb5647352ef67524))

* fix(V3): ensure display value is being hashed ([`dc5f2eb`](https://github.com/blockchain-certificates/cert-schema/commit/dc5f2eb5e93bdf398eaa6acf737b69977924f8ba))

* fix(v3): remove copy paste item ([`51f72d1`](https://github.com/blockchain-certificates/cert-schema/commit/51f72d15062b756809c62e60da1c50ae43f068dc))

* fix(v3): correct w3id path to schema ([`ba9c4f1`](https://github.com/blockchain-certificates/cert-schema/commit/ba9c4f164c21f45c1eb55d9b32837f6746bce8e2))

* fix(v3): properly expose items ([`30d8601`](https://github.com/blockchain-certificates/cert-schema/commit/30d8601ed6f1c6e98fbf26d87b03cf2bfbcba747))

* fix(Context): change copy paste error ([`9d37aad`](https://github.com/blockchain-certificates/cert-schema/commit/9d37aad9bd666d5bcc1fc61f1b22fdd675290af2))

* fix(ld): leverage w3id syntax ([`72b0710`](https://github.com/blockchain-certificates/cert-schema/commit/72b0710390c9dab8e4c7d4ed33f68a8147e210a7))

### Test

* test(v3): define id as non-relative value ([`3531682`](https://github.com/blockchain-certificates/cert-schema/commit/3531682d768c72bd833b7dc8e9263a5ac33c344d))

* test(All): ensure all tests are run ([`fd87426`](https://github.com/blockchain-certificates/cert-schema/commit/fd87426bd6393e98b98f9421589b93aa6486cc9b))

* test(V3): add custom contexts tests ([`968368f`](https://github.com/blockchain-certificates/cert-schema/commit/968368f017be5b8b0cd0b64ea53cb92fe22b77da))

* test(3.0-beta): updated contexts ([`085b226`](https://github.com/blockchain-certificates/cert-schema/commit/085b226b7a5a821e29d5e51233fba075c5a6212d))

### Unknown

* Merge branch &#39;master&#39; of https://github.com/blockchain-certificates/cert-schema into chore/npm-package ([`4d39ba5`](https://github.com/blockchain-certificates/cert-schema/commit/4d39ba54d5d7d15abfb0060b3fe68b87f0a0f9a0))

* Merge pull request #35 from blockchain-certificates/test/hashing

Test/hashing ([`81de83f`](https://github.com/blockchain-certificates/cert-schema/commit/81de83fc1eaf0c7cf328a54c9ec341c3211a71cd))

* Merge pull request #34 from blockchain-certificates/fix/v3-display

fix(V3): ensure display value is being hashed ([`bb68ca1`](https://github.com/blockchain-certificates/cert-schema/commit/bb68ca150dee691816869077c95a4dd9bc353d4e))

* Merge pull request #33 from blockchain-certificates/lemoustachiste-patch-1

fix(v3): remove copy paste item ([`659a375`](https://github.com/blockchain-certificates/cert-schema/commit/659a375d79669e4fa616740d0ea35756162522aa))

* Merge pull request #32 from blockchain-certificates/fix/schema-url

fix(v3): correct w3id path to schema ([`b547b48`](https://github.com/blockchain-certificates/cert-schema/commit/b547b4868dac15e44c0f4d92630cfd0e656f81ff))

* Merge pull request #31 from blockchain-certificates/feat/v3-final

feat(v3): fix v3 tests ([`c94605a`](https://github.com/blockchain-certificates/cert-schema/commit/c94605ac8f67addf443113418046138bf8dbabfe))

* Merge pull request #30 from blockchain-certificates/feat/v3-final

feat(v3): prepare code for v3 ([`4ddd495`](https://github.com/blockchain-certificates/cert-schema/commit/4ddd495245921b3e248c5cc404ead5d7ee3c1f89))

* Merge pull request #29 from blockchain-certificates/feat/v3

feat(V3): define v3 properties and versionning ([`37f10df`](https://github.com/blockchain-certificates/cert-schema/commit/37f10df50428c2db19255e4f598099dadb7b468b))

* Merge pull request #28 from blockchain-certificates/feat/v3-beta

feat(v3b): define more keys for blockcerts model ([`5300471`](https://github.com/blockchain-certificates/cert-schema/commit/5300471b8de5a4acc4663af660392dea54a679d9))

* Merge branch &#39;master&#39; of https://github.com/blockchain-certificates/cert-schema into feat/v3-beta ([`f9fecef`](https://github.com/blockchain-certificates/cert-schema/commit/f9fecefb9f29a07c03af4ea16e53ffbb855d135e))

* Merge pull request #26 from blockchain-certificates/feat/v3-beta

feat(v3b): prepare package for release ([`550f828`](https://github.com/blockchain-certificates/cert-schema/commit/550f82808b7415ff44b83aa1ef0690e5a633f6f8))

* Revving to b3 ([`bf2d142`](https://github.com/blockchain-certificates/cert-schema/commit/bf2d1428095289104642f92a3e8ba6a7566b533a))

* Merge pull request #23 from blockchain-certificates/feat/v3-beta

Feat/v3 beta ([`e602103`](https://github.com/blockchain-certificates/cert-schema/commit/e602103dc856ee7527226fd7370d9435ce201a48))

* Merge pull request #25 from bonn1112/feat/v3-beta

add v3-beta json file ([`bbc0da6`](https://github.com/blockchain-certificates/cert-schema/commit/bbc0da63e9e0f690bed356f78b622536817eb800))

* add v3-beta json file ([`9da6f24`](https://github.com/blockchain-certificates/cert-schema/commit/9da6f24fea335738b3538392d0a910840b80c262))

* Merge pull request #24 from bonn1112/feat/v3-beta

add import validater ([`f735f24`](https://github.com/blockchain-certificates/cert-schema/commit/f735f241585bdb2dcbc76eee5f6c7243edbe63c4))

* import validater ([`926bfff`](https://github.com/blockchain-certificates/cert-schema/commit/926bfffa45d0ce033e9708dcfa64592c4af73929))

* doc(3.0-beta): added doc ([`b154dd5`](https://github.com/blockchain-certificates/cert-schema/commit/b154dd5b902c4ca3341e99277a9ccade519f7a83))

* doc(30Beta): missing ssl protocols ([`f45d3fa`](https://github.com/blockchain-certificates/cert-schema/commit/f45d3fae55972592c5db5ee1e512b249247d2d87))

* Merge branch &#39;feat/v3-beta&#39; of https://github.com/blockchain-certificates/cert-schema into feat/v3-beta ([`d0a29f8`](https://github.com/blockchain-certificates/cert-schema/commit/d0a29f8fdb75ff0834325e7b4f5a87214075705d))

* doc(3.0-beta): removed false description ([`aafd7da`](https://github.com/blockchain-certificates/cert-schema/commit/aafd7dadb1838233061116158ec3c242869982fc))

* Merge pull request #22 from blockchain-certificates/update-merkleproof2019-link

update link ([`96c3e42`](https://github.com/blockchain-certificates/cert-schema/commit/96c3e423ce0dec046c7d080fe384dacd51316efa))

* update link ([`1d4dac8`](https://github.com/blockchain-certificates/cert-schema/commit/1d4dac8f44af90c241080a71f4eec44492865fe4))

* Revving version to republish PyPI package. ([`fc2652a`](https://github.com/blockchain-certificates/cert-schema/commit/fc2652a9426061edfd605aaf487fc098dbcb8528))

* Merge pull request #20 from blockchain-certificates/v3

Export V3 contexts/schemas &amp; V3 cert validation additions ([`30dbc38`](https://github.com/blockchain-certificates/cert-schema/commit/30dbc380b141b5e9829a613fb28c82f32e241bff))

* Adding option to ignore proof when validating an unsigned cert ([`1ef93e6`](https://github.com/blockchain-certificates/cert-schema/commit/1ef93e6ca11026891c8d0a3483a41f3bffc1c64a))

* Adding Verifiable Credential context to library exports ([`35be736`](https://github.com/blockchain-certificates/cert-schema/commit/35be7362f1411dd3b9a146d4408369515ccc86ca))

* Merge pull request #19 from blockchain-certificates/v3

Export V3 contexts/schemas to be used in a library ([`2f90254`](https://github.com/blockchain-certificates/cert-schema/commit/2f90254ca58212e4392881a9d5f6db0b1bed7d91))

* Export V3 contexts/schemas to be used in a library ([`66a7789`](https://github.com/blockchain-certificates/cert-schema/commit/66a77895ba10e18987fec0f5257332366bc2c3a6))

* Merge pull request #18 from blockchain-certificates/v3

Adding more MerkleProof2019 properties to context ([`c9e58e9`](https://github.com/blockchain-certificates/cert-schema/commit/c9e58e945d64044798b0ed09602c181915e9e46c))

* Adding more MerkleProof2019 properties to context ([`73dc356`](https://github.com/blockchain-certificates/cert-schema/commit/73dc356041580d72efacd0d2d7f6c09e77f604dd))

* Merge pull request #17 from blockchain-certificates/v3

Update bc v3 context to correct some security contexts ([`1e6d079`](https://github.com/blockchain-certificates/cert-schema/commit/1e6d0791f02f87cdbe60eedd7f638e87e586770b))

* Update bc v3 context to correct some security contexts ([`6617519`](https://github.com/blockchain-certificates/cert-schema/commit/6617519e8c001f60eaa6e48bffd91e3378d625e9))

* Merge pull request #16 from blockchain-certificates/v3

Fixing 3.0-alpha schema &amp; examples ([`3f6dcfc`](https://github.com/blockchain-certificates/cert-schema/commit/3f6dcfc7f46bc6b500a5339ff67e9dc072f028cd))

* Bump to 3.0.0a3 ([`b449168`](https://github.com/blockchain-certificates/cert-schema/commit/b4491682d3b6fe5533e5ada179fabf8ad68e9269))

* Schema updates for blockcerts type of verifiable credentials ([`59e1f82`](https://github.com/blockchain-certificates/cert-schema/commit/59e1f826d085205150f608ecdebe25a5a6459ab8))

* Merge pull request #12 from blockchain-certificates/v3

Fixing v3-alpha schema ([`b3d9f93`](https://github.com/blockchain-certificates/cert-schema/commit/b3d9f937313ba9eba6c4bb2eb59d6206d80aacc4))

* Bump v3-alpha version ([`9d58742`](https://github.com/blockchain-certificates/cert-schema/commit/9d5874238283b80e8e5278febf1b04211d7e2fa7))

* Remove old/conflicting schema references in v3 ([`3d6f681`](https://github.com/blockchain-certificates/cert-schema/commit/3d6f681f9028b71c87127c9207ea4ae3d376f1cc))

* Fix v3 reference link ([`4374b7d`](https://github.com/blockchain-certificates/cert-schema/commit/4374b7d87218bd842b9c27c0d79da2700377318f))

* Update bbba8553-8ec1-445f-82c9-a57251dd731c.json ([`f608739`](https://github.com/blockchain-certificates/cert-schema/commit/f60873943f1d975346ff40519bacd2473ec3dac0))

* Update README.md ([`6cf90f2`](https://github.com/blockchain-certificates/cert-schema/commit/6cf90f277e4655b260c572977c2cc32e7fca8cf2))

* Merge pull request #10 from blockchain-certificates/v3

PyPI Updates V3 ([`bce6b9b`](https://github.com/blockchain-certificates/cert-schema/commit/bce6b9bc28634d64dea192513a0455741f1b8521))

* Merge remote-tracking branch &#39;origin/v3&#39; into v3 ([`53df114`](https://github.com/blockchain-certificates/cert-schema/commit/53df11406489e508e07eb4074baeb3dd381304aa))

* Updating v3 for publishing to pypi ([`7a6af7c`](https://github.com/blockchain-certificates/cert-schema/commit/7a6af7c3c36080c1bdf59eac2067dd45f8048a25))

* Merge pull request #9 from blockchain-certificates/v3

V3 ([`d3aabc1`](https://github.com/blockchain-certificates/cert-schema/commit/d3aabc105e6f54ba75306ac769f293ef1e042a1c))

* Update README.md ([`30da460`](https://github.com/blockchain-certificates/cert-schema/commit/30da460c714845e0bce99ab283e422f130ecee3a))

* Merge pull request #7 from davidlj95/unknown-eth-testnet

Remove ambiguous ethereumTestnet from anchor chains ([`67b5467`](https://github.com/blockchain-certificates/cert-schema/commit/67b5467b88bc4cbd5fcd59af516dcc429c5917d6))
