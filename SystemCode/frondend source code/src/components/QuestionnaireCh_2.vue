<template>
    <v-app>
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'work'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    您在工作中对电脑的使用更符合以下哪种描述？
                    <template v-slot:actions>
                        <v-icon v-if="software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="software" column>
                        <v-radio
                                label="日常办公软件使用"
                                color="orange darken-3"
                                value='2D'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="可能占用高内存的软件使用"
                                color="orange darken-3"
                                value='3D'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="大量的程序项目"
                                color="orange darken-3"
                                value='DP'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    电脑是否需要商务外形（在正式场合不突兀）？
                    <template v-slot:actions>
                        <v-icon v-if="business_look === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="business_look !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="business_look" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="否"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel
                    v-if=" software == '2D'"
            >
                <v-expansion-panel-header disable-icon-rotate>
                    请指出以下可能需要的日常办公的软件：
                    <template v-slot:actions>
                        <v-icon v-if="work_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="work_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="work_software_value in work_software_values.slice(0,4)"
                            :key="work_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="work_software"
                            :label="work_software_value"
                            :value="work_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel
                    v-else-if=" software == '3D'"
            >
                <v-expansion-panel-header disable-icon-rotate>
                    请指出以下可能需要的占用高内存的软件：
                    <template v-slot:actions>
                        <v-icon v-if="highram_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="highram_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="highram_software_value in highram_software_values.slice(0,4)"
                            :key="highram_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="highram_software"
                            :label="highram_software_value"
                            :value="highram_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel
                    v-else
            >
                <v-expansion-panel-header disable-icon-rotate>
                    请指出以下可能需要在电脑上运行的软件：
                    <template v-slot:actions>
                        <v-icon v-if="deep_software === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="deep_software !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="deep_software_value in deep_software_values.slice(0,4)"
                            :key="deep_software_value"
                            multiple
                            color="orange darken-3"
                            v-model="deep_software"
                            :label="deep_software_value"
                            :value="deep_software_value"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你非常看重笔记本的电脑的哪些方面：
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!-- 学习 -->
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'study'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你学习中对电脑的使用？
                    <template v-slot:actions>
                        <v-icon v-if="study_purpose === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="study_purpose !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="study_purpose" column>
                        <v-radio
                                label="浏览网页或使用OFFICE软件"
                                color="orange darken-3"
                                value='reading'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="软件仿真和代码编写"
                                color="orange darken-3"
                                value='coding'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="处理大数据和训练神经网络"
                                color="orange darken-3"
                                value='deeplearning'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你非常看重笔记本的电脑的哪些方面：
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'game'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    您是否对大型单机游戏非常感兴趣？
                    <template v-slot:actions>
                        <v-icon v-if="game_3A === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="game_3A !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="game_3A" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='3A'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    平常玩游戏注意力会比较倾向于特效吗？
                    <template v-slot:actions>
                        <v-icon v-if="game_effect === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="game_effect !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="game_effect" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你非常看重笔记本的电脑的哪些方面：
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!--视频-->
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
                v-if="purpose == 'video'"
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你非常看重笔记本的电脑的哪些方面：
                    <template v-slot:actions>
                        <v-icon v-if="constraint === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="constraint !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-checkbox
                            v-for="i in constraint_values.slice(0,5)"
                            :key="i.index"
                            multiple
                            color="orange darken-3"
                            v-model="constraint"
                            :label="i.index"
                            :value="i.name"
                    >
                    </v-checkbox>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>


        <!--        &lt;!&ndash;提交按钮&ndash;&gt;-->
        <div>
            <v-btn
                    rounded
                    class="ma-2"
                    color="primary"
                    dark
                    v-on:click="submit"
            >提交
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
        </div>


        <!--进度条组件-->
        <v-progress-linear
                fixed
                background-opacity="0.3"
                :value="degree"
                color="primary"
        ></v-progress-linear>


        <!--浮动按钮-->
        <v-speed-dial
                v-model="fab"
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        v-model="fab"
                        color="blue darken-2"
                        dark
                        fab
                >
                    <v-icon v-if="fab">mdi-close</v-icon>
                    <v-icon v-else>mdi-menu</v-icon>
                </v-btn>
            </template>
            <v-btn
                    fab
                    dark
                    small
                    color="green"
            >
                En/Ch
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="indigo"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="red"
            >
                <v-icon>mdi-account-circle</v-icon>
            </v-btn>
        </v-speed-dial>
    </v-app>
</template>

<script>
    export default {
        name: "QuestionnaireCh_2",
        data() {
            return {
                // 第1页问题答案
                price: '',
                brand: [],
                purpose: '',
                rgb_require: '',
                bringout: '',
                screen: '',

                // 第2页问题答案
                software: '',
                study_purpose: '',
                game_3A: '',
                constraint: '',

                // 无用答案
                business_look: '',
                work_software: '',
                highram_software: '',
                deep_software: '',
                game_effect: '',

                // 问题选项
                work_software_values: ['OFFICE 三件套', '小型编程项目，数据处理项目', '二维制图软件，平面设计软件', '其他'],
                highram_software_values: ['使用视频剪辑软件', '3D建模软件', '虚拟机', '其他'],
                deep_software_values: ['大型工程项目', '大数据运算', '神经网络训练', '其他'],
                constraint_values: [
                    {index: '价格', name: 'price'},
                    {index: '品牌', name: 'brand'},
                    {index: '重量', name: 'weight'},
                    {index: '续航', name: 'battery_life'},
                    {index: '屏幕尺寸', name: 'screen_size'},
                ],

                // 功能变量
                fab: false, // 浮动按钮显示
                active_question: 0,
                degree: '',  // 控制进度条
                num_question: 3,
                num_ans: 0, //已回答问题数
            }
        },
        created() {
            this.price = this.$route.params.price;
            this.brand = this.$route.params.brand;
            this.purpose = this.$route.params.purpose;
            this.rgb_require = this.$route.params.rgb_require;
            this.bringout = this.$route.params.bringout;
            this.screen = this.$route.params.screen;

            if (this.purpose == 'work') {
                this.num_question = 3
            } else if (this.purpose == 'study') {
                this.num_question = 1
            } else if (this.purpose == 'game') {
                this.num_question = 2
            } else if (this.purpose == 'video') {
                this.num_question = 0
            }

        },
        methods: {
            submit() {
                // 跳转到下一页
                this.$router.push(
                    {
                        name: 'Output',
                        params: {
                            price: this.price,
                            purpose: this.purpose,
                            brand: this.brand,
                            rgb_require: this.rgb_require,
                            bringout: this.bringout,
                            screen: this.screen,
                            software: this.software,
                            study_purpose: this.study_purpose,
                            game_3A: this.game_3A,
                            constraint: this.constraint,
                        }
                    });
            },

            jump() {
                // 计算完成情况
                let count_ans = 0;

                let flag = {
                    software: this.software,
                    study_purpose: this.study_purpose,
                    game_3A: this.game_3A,
                    constraint: this.constraint,
                    business_look: this.business_look,
                    work_software: this.work_software,
                    highram_software: this.highram_software,
                    deep_software: this.deep_software,
                    game_effect: this.game_effect,
                }

                for (let i = 0; i < Object.keys(flag).length; i++) {
                    if (Object.values(flag)[i] !== '') {
                        count_ans += 1
                    }
                }

                // 跳转到下一个问题
                this.active_question += 1

                // 控制进度条
                this.degree = count_ans / this.num_question * 100

            },
        }
    }
</script>

<style scoped>

</style>